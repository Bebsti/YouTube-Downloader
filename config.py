import os

class Config:
    API_ID = int(os.getenv("API_ID", 12584381))
    API_HASH = os.getenv("API_HASH", '')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '')
