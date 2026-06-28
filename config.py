"""
Application configuration.

Loads all secrets and configuration from the .env file.
"""

import os

from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Google Apps Script
GAS_URL = os.getenv("GAS_URL")
API_SECRET = os.getenv("API_SECRET")

# Validate required configuration
required = {
    "BOT_TOKEN": BOT_TOKEN,
    "GAS_URL": GAS_URL,
    "API_SECRET": API_SECRET,
}

missing = [key for key, value in required.items() if not value]

if missing:
    raise RuntimeError(
        f"Missing required environment variables: {', '.join(missing)}"
    )