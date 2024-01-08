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

SESSION = getenv("SESSION", "AgB1WUkHScaE9rwJTy4fopo53UptazU-1HoYPaze0U3WHVaw-Q-x3PclMxAQVloXEX2fNs_GA9Wk1dAUtW-OwmoGPjHOblpr8kCXUvTlGwm5jimt-dTHzjcCqQC-uEUC5twLItQMZ2uqGg-0F4L8kBw8zKylD42yOF7Y1WEMPxSODP8hZfjviiTz3EaDW4SS6HDf1u-luO9qFE54kXyrErTJmTuNpB9gHKdhBNAz5bRfud3iIQioD40jAe3aI14wVGHn1xo4v7EyQs98OW4pJyKc8af6Tb7dx1tUP6Vx3wBXPBGrBY2rio3f_WLWdwqucoqklvjCVmejvDlR94yBi58VAAAAAYgARbMA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Kayfina")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XaosResmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5751610471").split()))


FAILED = "https://telegra.ph/file/c3166102f1c949f1ea0f3.jpg"
