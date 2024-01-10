from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "12210813"))
API_HASH = getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")

BOT_TOKEN = getenv("BOT_TOKEN", "6062022905:AAFjFdASrtYtMokfFwJwvtkgf0rhgG9Nlj0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6181182367"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/TUd4YGAFbbGJATgRA")
START_IMG = getenv("START_IMG", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fe0.pxfuel.com%2Fwallpapers%2F801%2F244%2Fdesktop-wallpaper-black-music-music-notes-with-black-background.jpg&tbnid=vevgkyzaPQVNpM&vet=1&imgrefurl=https%3A%2F%2Fwww.pxfuel.com%2Fen%2Fdesktop-wallpaper-owdcm&docid=NZM8buVlTU6g1M&w=850&h=850&hl=az&source=sh%2Fx%2Fim%2Fm1%2F2&kgs=ef3394778768e42d")

SESSION = getenv("SESSION", "AgC8aomShgbZSJVtRY4sTjZ-DxKpaXt3hXs9dutuYV3UhJ4dheFZ1hTSuH75QST6VPwKpmh8r4zzaXt4yYXCAUSLSImzmls6kc7cStIrekeSuAOq_Vq2zs2nh2hlcbBS15VCQB3htuxpgGoHOEXOVxgZDGCjlm3Pta0BsyhWj8nJRCXAGUmaX9Gvjr0BOlmPPfIWrkofhlVhM2yo8YygWqebOOu7yJuIVf3GuYkqGdsmudSq2tbNMVZ-SRoQqVISbOrhDo4SLbjL9Jpt5jpwM7R8Fye7Dj7-uF9JxltwbuVR7465dIr73-swxQm-9fGFrrlZHEEXLwZwlHHfGpLDPySuAAAAAX_r4P0A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NezrinChatt")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NezrinLogo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6181182367").split()))


FAILED = "https://images.app.goo.gl/m5AaiP3R35CXSSbG6"
