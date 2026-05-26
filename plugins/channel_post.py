import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from helper.helper_func import encode
import re
#===============================================================#

@Client.on_message(filters.private & ~filters.command(['start', 'shortner','users','broadcast','batch','genlink','stats', 'pbroadcast', 'db', 'adddb', 'add_db', 'removedb', 'rm_db',  'ban', 'unban', 'addpremium', 'delpremium', 'premiumusers', 'request', 'profile']))
async def channel_post(client: Client, message: Message):
    if message.from_user.id not in client.admins:
        return await message.reply(client.reply_text)
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    caption = ""
    if message.video or (message.document and message.document.mime_type and message.document.mime_type.startswith("video/")):
        file_name = getattr(message.video, "file_name", None) or getattr(message.document, "file_name", None) or ""
        quality = ""
        match = re.search(r"(144p|240p|360p|480p|720p|1080p|1440p|2160p|4k)", file_name, re.IGNORECASE)
        if match:
            quality = match.group(1).lower()
        elif message.video and getattr(message.video, "height", None):
            quality = f"{message.video.height}p"

        if quality:
            caption = f'<a href="https://t.me/Infinix_Adult/24"><b>{quality} • ʙʏ ɪɴꜰɪɴɪx ᴀᴅᴜʟᴛ</b></a>'
        else:
            caption = '<a href="https://t.me/Infinix_Adult/24"><b>ʙʏ ɪɴꜰɪɴɪx ᴀᴅᴜʟᴛ</b></a>'
    elif message.document or message.photo:
        caption = '<a href="https://t.me/Infinix_Adult/24"><b>ʙʏ ɪɴꜰɪɴɪx ᴀᴅᴜʟᴛ</b></a>'
        
    try:
        post_message = await message.copy(chat_id = client.db, caption=caption, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db, caption=caption, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b>Here is your link</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)

    if not client.disable_btn:
        await post_message.edit_reply_markup(reply_markup)

#===============================================================#

@Client.on_message(filters.channel & filters.incoming)
async def new_post(client: Client, message: Message):
    if message.chat.id != client.db:
        return
    if client.disable_btn:
        return

    converted_id = message.id * abs(client.db)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)

        pass





