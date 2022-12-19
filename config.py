import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "21849173")
        self.API_HASH: str = os.environ.get("API_HASH", "5d4ae6614b45dc890f3cbe3980c493f3")
        self.SESSION: str = os.environ.get("SESSION", "AQBUa3P0U8HfcilFtPP84n6M4oTPhSWDqiDR2c-kCa4AMt46xk4TcoTi-Tf8-piRcZfF1JiQPXdoM2Q7zzAA5HdD0oVnnODtWdW_Df8irPCDcd4hbVtEWmiZFQLU4gYuNn-G5Mxk2_q8waPDv6B0FIuMJbugq7XD1Jm3T_t7rmwjbPXlX7QV8EcZb1JIJlncUo4toHovq9DU3egqND9vtWVFgnx_i3eBNpYQ2BfNW3yT0plDV892D3nOW8NGdHKO51yv1ehhtY4PWCEGPKF7WdYct8F6KtdpsHY0WqtR91MHKPSNfa_CXOVc-YaWL8viCNK6Pie4RtkZBE_iqgwuqg9EAAAAAUfAUeYA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5939117192:AAEDVAjbrP25z7n8DNIPIQOqc1OeACat4Xo")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5498753510").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", "586ba3b44c5f437c853585359f57ec52")
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", "0e7242f6ce70419bbd1fac18848ab26b")


config = Config()
