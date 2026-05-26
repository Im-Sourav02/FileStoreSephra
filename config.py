import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 6123108288

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com" # shortner url 
SHORT_API = "573350da0e10a5a44f7e6fec3bc2b3f836b47805" 
SHORT_TUT = "https://t.me/Infinix_Tutorial/10"

# Bot Configuration
SESSION = "yato"
TOKEN = "7879774851:AAGsYcQ4kERZaB9TxmYX1RjqgGsqH6DdhFY"
API_ID = "21446955"
API_HASH = "e6f34a6186963663342b88b88c2b4750"
WORKERS = 5

DB_URI = "mongodb+srv://souravagarwal14092007:szXRs8g7fErCnn4@cluster0.xlsbf3o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Cluster0"

FSUBS = [[-1002345643351, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1002558171315   # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [6123108288]
# Bot Settings
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ʟᴏᴠᴇ ᴘᴏʀɴ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b><blockquote>◈ ᴏᴡɴᴇʀ : <a href=t.me/Im_Sukuna02>ɪᴍ•Ꮪᴜ͢ᴋᴜɴᴀ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/InfinixSyndicate>ɪɴғɪɴɪx sʏɴᴅɪᴄᴀᴛᴇ</a>\n◈ ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Infinix_Movie>ɪɴғɪɴɪx ᴍᴏᴠɪᴇs</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Im_Sukuna02>Sᴜᴋᴜɴᴀ</a></blockquote></b>",
    "REPLY": "<b>For More Join - @Infinix_Adult</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://i.ibb.co/YBMNRYcV/photo-2025-05-23-09-40-37-7507573799429079152.jpg",
    "FSUB_PHOTO": "https://i.ibb.co/w8pj89D/photo-2025-05-26-09-47-35-7509204022985752700.jpg",
    "SHORT_PIC": "https://i.ibb.co/kVQTwH6Z/x.jpg",
    "SHORT": "https://i.ibb.co/w8pj89D/photo-2025-05-26-09-47-35-7509204022985752700.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
