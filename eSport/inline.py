from eSport.config import UPDATES_CHANNEL, GROUP_SUPPORT
from pyrogram import Client, errors
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0

def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="ð¨ð½ð±ð®ðð²ð ð±", url=f"https://t.me/{UPDATES_CHANNEL}"),
      InlineKeyboardButton(text="ððð½ð½ð¼ð¿ð ð©", url=f"https://t.me/{GROUP_SUPPORT}"),
    ],
    [
      InlineKeyboardButton(text="â¢ CÊá´sá´", callback_data=f'cls'),
    ],
  ]
  return buttons

def stream_markup(user_id, dlurl):
  buttons = [
    [
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="â·", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="â£â£I", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="â¢", callback_data=f'cbstop | {user_id}')
    ],
    [
      InlineKeyboardButton(text="ð¨ð½ð±ð®ðð²ð ð±", url=f"https://t.me/{UPDATES_CHANNEL}"),
      InlineKeyboardButton(text="ððð½ð½ð¼ð¿ð ð©", url=f"https://t.me/{GROUP_SUPPORT}"),
    ],
    [
      InlineKeyboardButton(text="á´Êá´sá´", callback_data=f'cls'),
    ],
  ]
  return buttons

def menu_markup(user_id):
  buttons = [
     [InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="â·", callback_data=f'cbresume | {user_id}')],
     [InlineKeyboardButton(text="â£â£I", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="â¢", callback_data=f'cbstop | {user_id}')
    ],
     [InlineKeyboardButton(text="ð", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="á´á´©á´á´á´á´s", url=f"https://t.me/BotDuniyaXd"),
      InlineKeyboardButton(text="ð", callback_data=f'cbunmute | {user_id}')],
  ]
  return buttons

def song_download_markup(videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="â¬ï¸ á´á´á´Éªá´",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="â¬ï¸ á´ Éªá´á´á´",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Êá´á´á´",
                callback_data="cbhome",
            )
        ],
    ]
    return buttons

close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "â¢ á´Êá´sá´ â¢", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "â¢ Êá´á´á´ â¢", callback_data="cbmenu"
      )
    ]
  ]
)
