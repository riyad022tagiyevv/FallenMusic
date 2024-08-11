from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24548143"))
API_HASH = getenv("API_HASH", "6cba049c135a0393615878ea1e3c9443")

BOT_TOKEN = getenv("BOT_TOKEN", "7356145623:AAEfeB8yGbQMd_CIeAuMGUQalj6gob7MSXI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID","6634423600"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AgF2ky8AjSzO6Wbk5lzM3wXSPdcFm7p0pcupRNkmOdmweQGt15jlGgWAWkNvys3ddjLU-IpPilm-LOpc1qJx07N4wFmgvyt46BSpguHnxRhoyzBNWZeJx47v1c1rAJzCIMNAUgpdfA308oC-xA3Z6SQxvx7HMmeMjOiHf-pxrvPQpr9paB0hDlPHpUookO6xO_8b4quOOT-EUnGRIs70-998l0xIRzoQsqNoFcNv2VGq6jy98l8xsUA7ThEJPnaeMTrxI-5I_4fBQ9FBrA0IbdUpCYPubwf_jqCk17nFLf2edZh1KLQ6w0mXaDXXvrHbvZQd5cKl0vWbhI_QDGwS8ILGs7YyoAAAAAGLGQbjAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nezrinsupp")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/nezrinlogo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6634423600").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
