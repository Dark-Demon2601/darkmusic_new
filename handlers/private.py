from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import BOT_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d5c3597f2df22173a78bd.png",
        caption=f"""**➮𝐳 ʜɪɪ ɪ ᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
➮ Doreamon Sყʂƚҽɱ Wσɾƙιɳɠ Fιɳҽ
➮ Doreamon ᴠᴇʀꜱɪᴏɴ : 1.0 Lҽƚҽʂƚ
➮ ᴍʏ ᴏᴡɴᴇʀ : [{TOXIC}](https://t.me/akshi_s_ashu1)
➮ **ꜱᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ : {uptime}**
𝚃𝚑𝚊𝚗𝚔𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 Doreamon 𝙱𝚘𝚝 ♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/phoenix_music_suport}"
                    
                   ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/phoenix_music_new}"
                   
                    )
                ]
            ]
        )
    )
