"""
BudgetBot entry point.
"""

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN

from constants import (
    FLOW_CATEGORY,
    AMOUNT,
    ACCOUNT,
    CATEGORY,
    NOTE,
    CONFIRM,
)

from common import (
    start,
    help_command,
    cancel,
)

from log import (
    start_flow,
    receive_flow,
    receive_amount,
    receive_account,
    receive_category,
    receive_note,
    confirm_expense,
)


def main():

    application = Application.builder().token(BOT_TOKEN).build()

    expense_handler = ConversationHandler(
        entry_points=[
            CommandHandler("log", start_flow)
        ],

        states={
            FLOW_CATEGORY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    receive_flow,
                )
            ],

            AMOUNT: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    receive_amount,
                )
            ],

            ACCOUNT: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    receive_account,
                )
            ],

            CATEGORY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    receive_category,
                )
            ],

            NOTE: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    receive_note,
                )
            ],

            CONFIRM: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    confirm_expense,
                )
            ],
        },

        fallbacks=[
            CommandHandler("cancel", cancel)
        ],
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(expense_handler)

    print("BudgetBot is running...")

    application.run_polling()


if __name__ == "__main__":
    main()