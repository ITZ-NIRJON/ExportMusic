import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NirjonWorldMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "NixaWorld")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6190680150").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1909f1b61beb982a5d577.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-NIRJON/ExportMusic")
IMG = getenv("IMG", "https://te.legra.ph/file/7a707289b3f970a0ae59d.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
