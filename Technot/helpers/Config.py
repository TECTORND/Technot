import sys
import os
from typing import Set

from telethon.tl.types import ChatBannedRights
from validators.url import url
from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Config(object):
    # mandatory
    APP_ID = ((
        sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=None)
    DB_URL = (
        sys.argv[4]
        if len(sys.argv) > 4
        else config("DB_URL", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    BOT_USERNAME = None
    # get this value from http://www.timezoneconverter.com/cgi-bin/findzone.tzc
    TZ = config("TZ", default="Asia/Kolkata")
    AUTONAME = config("AUTONAME", default=None)
    # set this with required techno repo link
    UPSTREAM_REPO = config(
        "UPSTREAM_REPO", default="https://github.com/TeamTechnot/Technot"
    )
    EXTRA_REPO = config("EXTRA_REPO", default=None)
    if EXTRA_REPO and (EXTRA_REPO.lower() == "Yes") and not url(EXTRA_REPO):
        EXTRA_REPO = "https://github.com/TeamTechnot/Plugins"
    ADDONS = config("ADDONS", default=False)
    # Set this value with group id of private group(can be found this value by .id)
    PRIVATE_GROUP_BOT_API_ID = config("PRIVATE_GROUP_BOT_API_ID", default=0, cast=int)
    # Set this value same as PRIVATE_GROUP_BOT_API_ID if you need pmgaurd
    PRIVATE_GROUP_ID = config("PRIVATE_GROUP_ID", default=0, cast=int)
    # Set this value for working of fban/unfban/superfban/superunfban cmd
    FBAN_GROUP_ID = config("FBAN_GROUP_ID", default=0, cast=int)
    # set this value with channel id of private channel use full for .frwd cmd
    PRIVATE_CHANNEL_BOT_API_ID = config("PRIVATE_CHANNEL_BOT_API_ID", default=0, cast=int)
    # for heroku plugin you can get this value from https://dashboard.heroku.com/account
    API_KEY = config("API_KEY", default=None)
    # set this with same app name you given for heroku
    APP_NAME = config("APP_NAME", default=None)
    # Owner id to show profile link of given id as owner
    OWNER_ID = config("OWNER_ID", default=0, cast=int)
    # set this with group id so it keeps notifying about your tagged messages or pms
    PM_LOGGER_GROUP_ID = (
        config("PM_LOGGER_GROUP_ID", default=0, cast=int)
        or config("PM_LOGGR_BOT_API_ID", default=0, cast=int)
    )

    # Custom vars for Technot
    # set this will channel id of your custom plugins
    PLUGIN_CHANNEL = config("PLUGIN_CHANNEL", default=0, cast=int)
    # set this value with your required name for telegraph plugin
    TELEGRAPH_SHORT_NAME = config("TELEGRAPH_SHORT_NAME", default="technouserbot")
    # for custom thumb image set this with your required thumb telegraoh link
    THUMB_IMAGE = config(
        "THUMB_IMAGE", default="https://te.legra.ph/file/d882eee939a66432650b4.jpg"
    )
    # specify NO_LOAD with plugin names for not loading in Technot
    NO_LOAD = list(config("NO_LOAD", default="").split())
    # for custom pic for .digitalpfp
    DIGITAL_PIC = config("DIGITAL_PIC", default=None)
    # your default pic telegraph link
    DEFAULT_PIC = config("DEFAULT_PIC", default=None)
    # set this with your default bio
    DEFAULT_BIO = config("DEFAULT_BIO", default=None)
    # set this with your deafult name
    DEFAULT_NAME = config("DEFAULT_NAME", default=None)
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    HANDLER = config("HANDLER", default=r".")
    SUDO_HANDLER = config("SUDO_HANDLER", default=r".")
    # set this with required folder path to act as download folder
    TMP_DOWNLOAD_DIRECTORY = config("TMP_DOWNLOAD_DIRECTORY", default="downloads")
    # set this with required folder path to act as temparary folder
    TEMP_DIR = config("TEMP_DIR", default="./temp/")
    # SpamWatch, default=CAS, default=SpamProtection ban Needed or not
    ANTISPAMBOT_BAN = config("ANTISPAMBOT_BAN", default=False)
    # progress bar progress
    FINISHED_PROGRESS_STR = config("FINISHED_PROGRESS_STR", default="▰")
    UNFINISHED_PROGRESS_STR = config("UNFINISHED_PROGRESS_STR", default="▱")
    # For Your Channel  and Group
    YOUR_GROUP = config("YOUR_GROUP", default=None)
    YOUR_CHANNEL = config("YOUR_CHANNEL", default=None)
    # API VARS FOR USERBOT
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture for screen shot
    SCREEN_SHOT_LAYER_ACCESS_KEY = config("SCREEN_SHOT_LAYER_ACCESS_KEY", default=None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = config("OPEN_WEATHER_MAP_APPID", default=None)
    # This is required for the speech to text plugin. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = config("IBM_WATSON_CRED_URL", default=None)
    IBM_WATSON_CRED_PASSWORD = config("IBM_WATSON_CRED_PASSWORD", default=None)
    # Get free api from https://dashboard.ipdata.co/sign-up.html
    IPDATA_API = config("IPDATA_API", default=None)
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = config("OCR_SPACE_API_KEY", default=None)
    # Genius lyrics get this value from https://genius.com/developers both has
    GENIUS_API_TOKEN = config("GENIUS_API_TOKEN", default=None)
    # Get your own API key from https://www.remove.bg/
    REM_BG_API_KEY = config("REM_BG_API_KEY", default=None)
    # Get this value from https://free.currencyconverterapi.com/
    CURRENCY_API = config("CURRENCY_API", default=None)
    # Google Drive plugin https://telegra.ph/G-Drive-guide-for-technouserbot-01-01
    G_DRIVE_CLIENT_ID = config("G_DRIVE_CLIENT_ID", default=None)
    G_DRIVE_CLIENT_SECRET = config("G_DRIVE_CLIENT_SECRET", default=None)
    G_DRIVE_FOLDER_ID = config("G_DRIVE_FOLDER_ID", default=None)
    G_DRIVE_DATA = config("G_DRIVE_DATA", default=None)
    G_DRIVE_INDEX_LINK = config("G_DRIVE_INDEX_LINK", default=None)
    # For transfer channel 2 step verification code of telegram
    TG_2STEP_VERIFICATION_CODE = config("TG_2STEP_VERIFICATION_CODE", default=None)
    # JustWatch Country for watch plugin
    WATCH_COUNTRY = config("WATCH_COUNTRY", default="IN")
    # Last.fm plugin  https://telegra.ph/Guide-for-LASTFM-02-03
    BIO_PREFIX = config("BIO_PREFIX", default=None)
    LASTFM_API = config("LASTFM_API", default=None)
    LASTFM_SECRET = config("LASTFM_SECRET", default=None)
    LASTFM_USERNAME = config("LASTFM_USERNAME", default=None)
    LASTFM_PASSWORD_PLAIN = config("LASTFM_PASSWORD", default=None)
    # SpamWatch API you can get it from get api from http://t.me/SpamWatchBot?start=token
    SPAMWATCH_API = config("SPAMWATCH_API", default=None)
    # can get from https://coffeehouse.intellivoid.net/
    RANDOM_STUFF_API_KEY = config("RANDOM_STUFF_API_KEY", default=None)
    # github vars
    GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN", default=None)
    GIT_REPO_NAME = config("GIT_REPO_NAME", default=None)
    # Deepai value can get from https://deepai.org/
    DEEP_AI = config("DEEP_AI", default=None)

    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # specify LOAD and NO_LOAD
    LOAD = []
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHROME_BIN = config("CHROME_BIN", default="/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = config(
        "CHROME_DRIVER", default="/app/.chromedriver/bin/chromedriver"
    )
    # for sed plugin
    GROUP_REG_SED_EX_BOT_S = config(
        "GROUP_REG_SED_EX_BOT_S", default=r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    # time.py
    COUNTRY = str(config("COUNTRY", default=""))
    SPOTIFY_CLIENT_ID = config("SPOTIFY_CLIENT_ID", default=None)
    SPOTIFY_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET", default=None)
    TZ_NUMBER = config("TZ_NUMBER", default=1, cast=int)
    # For updater plugin
    UPSTREAM_REPO_BRANCH = config("UPSTREAM_REPO_BRANCH", default="master")
    # dont touch this at all
    SUDO_USERS: Set[int] = set()
    TECHNOTLOGO = None
    BOTLOG = False
    BOTLOG_CHATID = 0
    EXTRA_REPOBRANCH = config("EXTRA_REPOBRANCH", default="main")
