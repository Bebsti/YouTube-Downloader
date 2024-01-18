import os

class Config:
    API_ID = int(os.getenv("API_ID", 12584381))
    API_HASH = os.getenv("API_HASH", '4b9b35b543d9f483453002d5765ef544')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '')
