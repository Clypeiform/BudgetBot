"""
Functions for interacting with the Google Apps Script API.
"""

import requests

from config import GAS_URL, API_SECRET


def log_expense(
    flow_type: str,
    amount: float,
    bank_account: str,
    category: str,
    note: str = "",
) -> tuple[bool, str]:
    """
    Sends a flow to the Google Apps Script.

    Returns:
        (success, message)
    """

    payload = {
        "secret": API_SECRET,
        "flowType": flow_type,
        "amount": amount,
        "bankAccount": bank_account,
        "category": category,
        "note": note,
        "source": "Telegram",
    }

    try:
        response = requests.post(
            GAS_URL,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if data.get("ok"):
            return True, "Expense logged successfully."

        return False, data.get("error", "Unknown API error.")

    except requests.Timeout:
        return False, "The request timed out."

    except requests.RequestException as e:
        return False, str(e)

    except Exception as e:
        return False, str(e)