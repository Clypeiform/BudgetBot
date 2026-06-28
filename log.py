"""
Expense conversation handlers.
"""

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from api import log_expense
from constants import (
    ACCOUNT,
    ACCOUNTS,
    AMOUNT,
    FLOW_CATEGORY,
    FLOW_CATEGORIES,
    CATEGORY,
    INFLOW_CATEGORIES,
    OUTFLOW_CATEGORIES,
    CONFIRM,
    CONFIRM_BUTTON,
    CANCEL_BUTTON,
    NOTE,
    SKIP_BUTTON,
)
from keyboards import (
    account_keyboard,
    flow_keyboard,
    inflow_keyboard,
    outflow_keyboard,
    confirm_keyboard,
    note_keyboard,
)



async def start_flow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Entry point for /log
    """


    context.user_data.clear()

    await update.message.reply_text(
        "Select the flow type:",
        reply_markup=flow_keyboard(),
    )


    return FLOW_CATEGORY

    
async def receive_flow(update: Update, context: ContextTypes.DEFAULT_TYPE):

    flow = update.message.text.strip()

    if flow not in FLOW_CATEGORIES:
        await update.message.reply_text(
            "Please choose a flow using the keyboard."
        )
        return FLOW_CATEGORY

    context.user_data["flowType"] = flow

    await update.message.reply_text(
        "💵 Enter the amount:"
    )

    return AMOUNT

async def receive_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    

    

    await update.message.reply_text(
        "💵 Enter the flow amount:"
    )

    return AMOUNT


async def receive_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    try:
        amount = float(text)

        if amount <= 0:
            raise ValueError()

    except ValueError:
        await update.message.reply_text(
            "❌ Please enter a valid positive number."
        )
        return AMOUNT

    context.user_data["amount"] = amount

    await update.message.reply_text(
        "Select the account:",
        reply_markup=account_keyboard(),
    )

    return ACCOUNT


async def receive_account(update: Update, context: ContextTypes.DEFAULT_TYPE):

    account = update.message.text.strip()

    if account not in ACCOUNTS:
        await update.message.reply_text(
            "Please choose an account using the keyboard."
        )
        return ACCOUNT

    context.user_data["bankAccount"] = account

    if context.user_data["flowType"] == "Inflow":
        keyboard = inflow_keyboard()
    else:
        keyboard = outflow_keyboard()

    await update.message.reply_text(
        "Select the category:",
        reply_markup=keyboard,
    )

    return CATEGORY


async def receive_category(update: Update, context: ContextTypes.DEFAULT_TYPE):

    category = update.message.text.strip()

    if context.user_data["flowType"] == "Inflow":
        valid_categories = INFLOW_CATEGORIES
    else:
        valid_categories = OUTFLOW_CATEGORIES

    if category not in valid_categories:
        await update.message.reply_text(
            "Please choose a category using the keyboard."
        )
        return CATEGORY

    context.user_data["category"] = category

    await update.message.reply_text(
        "Enter a note (optional):",
        reply_markup=note_keyboard(),
    )

    return NOTE


async def receive_note(update: Update, context: ContextTypes.DEFAULT_TYPE):

    note = update.message.text.strip()

    if note == SKIP_BUTTON:
        note = ""

    context.user_data["note"] = note

    summary = (
        "Please confirm:\n\n"
        f"💵 Flow: {context.user_data['flowType']}\n"
        f"💵 Amount: ${context.user_data['amount']:.2f}\n"
        f"🏦 Account: {context.user_data['bankAccount']}\n"
        f"📂 Category: {context.user_data['category']}\n"
        f"📝 Note: {note or '-'}"
    )

    await update.message.reply_text(
        summary,
        reply_markup=confirm_keyboard(),
    )

    return CONFIRM


async def confirm_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):

    choice = update.message.text.strip()

    if choice == CANCEL_BUTTON:

        context.user_data.clear()

        await update.message.reply_text(
            "❌ Cancelled.",
            reply_markup=ReplyKeyboardRemove(),
        )

        return ConversationHandler.END

    if choice != CONFIRM_BUTTON:

        await update.message.reply_text(
            "Please choose Confirm or Cancel."
        )

        return CONFIRM

    success, message = log_expense(
        flow_type=context.user_data["flowType"],
        amount=context.user_data["amount"],
        bank_account=context.user_data["bankAccount"],
        category=context.user_data["category"],
        note=context.user_data["note"],
    )

    context.user_data.clear()

    if success:

        await update.message.reply_text(
            "✅ Expense logged successfully!",
            reply_markup=ReplyKeyboardRemove(),
        )

    else:

        await update.message.reply_text(
            f"❌ Failed to log expense.\n\n{message}",
            reply_markup=ReplyKeyboardRemove(),
        )

    return ConversationHandler.END