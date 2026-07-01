from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "30422005"))
        self.API_HASH = getenv("API_HASH", "5170ded206641d73215baf40175a6924")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "Apna Bot Token")
        self.MONGO_URL = getenv("MONGO_URL", "Apna Mongo Db Dalo")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003951821704"))
        self.OWNER_ID = int(getenv("OWNER_ID", "5940554521"))
        
        self.SESSION1 = getenv("SESSION", "Apna String Dalo")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SayaProject")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SayaProject")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "5400000000"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400000000"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20000000"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.catbox.moe/9csybn.jpeg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/8o5shi.jpg")
        self.START_IMG = [
            url.strip(" `\"'") 
            for url in getenv("START_IMG", "https://files.catbox.moe/cvpz1j.jpg https://files.catbox.moe/9csybn.jpeg https://files.catbox.moe/gbuf6w.jpg").replace("`", " ").split()
            if url.strip(" `\"'")
        ]

        self.XBIT_API_TOKEN = getenv("XBIT_API_TOKEN", None)
        self.XBIT_API_URL = getenv("XBIT_API_URL", None)
        self.ARU_API_KEY = getenv("ARU_API_KEY", None)
        self.ARU_API_URL = getenv("ARU_API_URL", None)
        self.GIT_REPO = getenv("GIT_REPO", "https://github.com/SayaProject")

    def check(self):
        missing = []
        if not self.API_ID: missing.append("API_ID")
        if not self.API_HASH: missing.append("API_HASH")
        if not self.BOT_TOKEN: missing.append("BOT_TOKEN")
        if not self.MONGO_URL or "Apna Mongo" in self.MONGO_URL: missing.append("MONGO_URL")
        if not self.OWNER_ID: missing.append("OWNER_ID")
        if not self.SESSION1 or "Apna String" in self.SESSION1: missing.append("SESSION")
        
        if missing:
            raise SystemExit(f"Missing required environment variables in .env: {', '.join(missing)}")
