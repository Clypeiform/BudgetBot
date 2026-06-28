"""
Application constants.

Everything in this file is safe to commit to Git.
"""

# ==========================================================
# Conversation States
# ==========================================================

(
    FLOW_CATEGORY,
    AMOUNT,
    ACCOUNT,
    CATEGORY,
    NOTE,
    CONFIRM,
) = range(6)


# ==========================================================
# Bank Accounts
# ==========================================================

ACCOUNTS = [
    "Mari Credit",
    "POSB Everyday",
    "Cash",
    "SC JumpStart",
    "UOB Absolute",
    "MariBank",
    "Youtrip",
    "Alipay",
    "WeChat",
    
]

# ==========================================================
# Flow Categories
# ==========================================================

FLOW_CATEGORIES = [
    "Inflow",
    "Outflow",
]

# ==========================================================
# Expense Categories
# ==========================================================

INFLOW_CATEGORIES = [
    "Salary",
    "PayNow Transfer",
    "SSB Interest",
    "Other",
]

OUTFLOW_CATEGORIES = [
    "Food",
    "Groceries",
    "Transport",
    "Shopping",
    "Entertainment",
    "Travel",
    "Medical",
    "Utilities",
    "Subscriptions",
    "Others",
]


# ==========================================================
# Keyboard Buttons
# ==========================================================

CONFIRM_BUTTON = "✅ Confirm"
CANCEL_BUTTON = "❌ Cancel"
SKIP_BUTTON = "⏭️ Skip"


# ==========================================================
# Commands
# ==========================================================

EXPENSE_COMMAND = "expense"
CANCEL_COMMAND = "cancel"
START_COMMAND = "start"
HELP_COMMAND = "help"