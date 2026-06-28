"""
Common command handlers.
"""

from telegram import ReplyKeyboardRemove
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /start
    """

    await update.message.reply_text(
        "👋 Welcome to BudgetBot!\n\n"
        "Use /log to log a flow."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /help
    """

    await update.message.reply_text(
        "Available commands:\n\n"
        "/log - Log a flow\n"
        "/cancel - Cancel the current operation\n"
        "/help - Show this message"
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Cancels any active conversation.
    """

    context.user_data.clear()

    await update.message.reply_text(
        "❌ Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END