"""
Telegram keyboard layouts.
"""

from telegram import ReplyKeyboardMarkup

from constants import (
    ACCOUNTS,
    FLOW_CATEGORIES,
    INFLOW_CATEGORIES,
    OUTFLOW_CATEGORIES,
    CONFIRM_BUTTON,
    CANCEL_BUTTON,
    SKIP_BUTTON,
)


def build_keyboard(items: list[str], columns: int = 2) -> ReplyKeyboardMarkup:
    """
    Build a ReplyKeyboardMarkup with the specified number of columns.
    """

    keyboard = []

    for i in range(0, len(items), columns):
        keyboard.append(items[i:i + columns])

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def account_keyboard():
    return build_keyboard(ACCOUNTS)


def flow_keyboard():
    return build_keyboard(FLOW_CATEGORIES)


def inflow_keyboard():
    return build_keyboard(INFLOW_CATEGORIES)


def outflow_keyboard():
    return build_keyboard(OUTFLOW_CATEGORIES)



def note_keyboard():
    return ReplyKeyboardMarkup(
        [[SKIP_BUTTON]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def confirm_keyboard():
    return ReplyKeyboardMarkup(
        [
            [CONFIRM_BUTTON, CANCEL_BUTTON],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )