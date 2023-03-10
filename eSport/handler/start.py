from cache.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from eSport.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from cache.filters import other_filters2
from time import time
from datetime import datetime
from cache.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)

start_keyboard = InlineKeyboardMarkup( [[
      InlineKeyboardButton("ðð¼ðºðºð®ð»ð±ð ð©", url=f"https://telegra.ph/ð©-Éªá´sÉ´ÉªÊá´á´É´ðª-02-27"), 
      ],[
      InlineKeyboardButton("ð±ðð¿ð¼ðð½", url=f"t.me/{GROUP_SUPPORT}"), 
      InlineKeyboardButton("ð¨ð½ð±ð®ðð²ð ð±", url=f"t.me/{UPDATES_CHANNEL}"), 
      ],[
      InlineKeyboardButton("â ððð ð ð ðððð¬ â", url=f"t.me/{BOT_USERNAME}?startgroup=True")
      ]]
      ) 


@Client.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        text=f"**ððð¥ð¥ð¨ {message.from_user.mention()}\n\nð¥ðð¡ð¢ð¬ {BOT_NAME}ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ \nðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð \nðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ðð¤ \nâ­ððð¯ðð¥ð¨ð©ðð ðð² [ððð©ð¨ð«ð­ððð«ð¯ðð«](https://t.me/NixaWorld)ð..**", 
        disable_web_page_preview=True,
        reply_markup=start_keyboard, 
    ) 
        
