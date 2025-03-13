import os
import logging
from logging.handlers import RotatingFileHandler


def get_int_env(var_name, default):
    try:
        return int(os.environ.get(var_name, default))
    except ValueError:
        return default  # Fallback to default if conversion fails


def str_to_bool(value):
    return str(value).lower() in ("true", "1", "yes")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "8176887548:AAELsQbL0CxdXlCuBm69WqbMA4XrSO3gOig")
API_ID = get_int_env("API_ID",25956970)
API_HASH = os.environ.get("API_HASH", "5fb73e6994d62ba1a7b8009991dd74b6")

OWNER_ID = get_int_env("OWNER_ID", 1074804932)
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ygovcu:fY1f9Wovol3NqhUX@cluster0.1mdno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

CHANNEL_ID = get_int_env("CHANNEL_ID", -1002358588449)
FORCE_SUB_CHANNEL = get_int_env("FORCE_SUB_CHANNEL", -1002358532189)
FORCE_SUB_CHANNEL2 = get_int_env("FORCE_SUB_CHANNEL2", -1001657207796)
FORCE_SUB_CHANNEL3 = get_int_env("FORCE_SUB_CHANNEL3", -1002335038787)
FORCE_SUB_CHANNEL4 = get_int_env("FORCE_SUB_CHANNEL4", -1001476099980)

FILE_AUTO_DELETE = get_int_env("FILE_AUTO_DELETE", 900)  # Auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 6)

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/c08dce4bf812fdd47bb69-7c17d1d0fc2c5c5b60.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/f3eac1f8e3d8f7c8f22f7-98d0f1327656800293.jpg")

# Proper handling of admins
ADMINS = {1074804932}  # Use a set to avoid duplicates
env_admins = os.environ.get("ADMINS", "1074804932").split()
ADMINS.update(int(x) for x in env_admins if x.isdigit())  # Ensuring only valid numbers
ADMINS.add(OWNER_ID)  # Ensuring OWNER_ID is in ADMINS
ADMINS = list(ADMINS)  # Convert back to list for compatibility

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = str_to_bool(os.environ.get('PROTECT_CONTENT', "False"))
DISABLE_CHANNEL_BUTTON = str_to_bool(os.environ.get('DISABLE_CHANNEL_BUTTON', "True"))

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Orey!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE",
                           "Hello {mention}\n\n<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ. \n\n ..:) 🥰</b>")

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
