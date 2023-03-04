import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "23489281")
        self.API_HASH: str = os.environ.get("API_HASH", "5fd3d83fa943f0f3d05bf1964a6d77f3")
        self.SESSION: str = os.environ.get("SESSION", "BQCmlWUTtuk9O9JqKzrwVjbiZA5fJv7bNgL4CqMeJ4y57nYxFTK6yN1kPE3F1TaAOfto-ph3QByA8oTGALS-dqJ_OWs1aC3lL1UOI4QgK95sxCz2tWFYo1IhWzMN-ov3Gq8M4LGJ5L7rRdQ7M8pf9kWuuRW9WITXAEDzvmKMuN37bIBwwOnG3HAsARiU6Fkk1fFDLWzR0uQ8wFceGQYFYwdaGaXXQb-udTQ9kUeq_afFUYnH9i5q4wlQbMZBNTgpy33LgPS_c9HRxNva3C3h8y6JNKrD_HYFiT8kS6Oi0XSFUGEv3oArtvFzatE_PSVxw8P-5ldeTcu4TmpSBzis3bUHAAAAAWiCwroA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "6257547712:AAHgzrWZDZWOBdxKSYtNaWAG8VpFDr9TVMI")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "6048367290").split() if id.isnumeric()
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
