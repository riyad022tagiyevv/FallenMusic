from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "12349641"))
API_HASH = getenv("API_HASH", "0f9159afc920f9c592df555e4b1cb73b")

BOT_TOKEN = getenv("BOT_TOKEN", "7260216865:AAFamWUlEDkPZQJk2MGrrzR_4bH3P3bR3ck")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID","6634423600"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AgC8cMkAEu5DkJov1ryum0wtNdQ9vuQAvdMYvb1uLEee_v82Ru2v7bDh7aI6H50q_r4rSl8NQyMCBIQPxgOIoLmFeMWq1CUQ_iLBpkJZ3bl6ukpmJSUUOHBNJtYiGr7TMbkzP_CCDHKOIgTQKC9T1And7k02gn1SHEYv-iZs6V0WMHlX0YTFmR8ZJb79-j0bHOsl2E9I_V0iGUINdHWMdBKcYkFMR7gPA-Umyc7wV5jnkkFrM6Tua-U280IvzhPGoCMPublZh2TdB3QtsGeE75RbA3ZXwQY-P_tjvNyIoAyHEknZ1g-krf4gUNSv384PO1g345l2mE6qB0NXUi3osw1hk97FVQAAAAG6f94tAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nezrinsupp")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/nezrinlogo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6634423600").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
