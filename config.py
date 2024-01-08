from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "12210813"))
API_HASH = getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")

BOT_TOKEN = getenv("BOT_TOKEN", "6062022905:AAFjFdASrtYtMokfFwJwvtkgf0rhgG9Nlj0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5663585448"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7939203c81ffee91e1a1.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c3166102f1c949f1ea0f3.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Kayfina")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XaosResmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5751610471").split()))


FAILED = "https://telegra.ph/file/c3166102f1c949f1ea0f3.jpg"
