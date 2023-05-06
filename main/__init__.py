#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 6216349
API_HASH = 5c7418e9f3df6db931caa7354521c55f
BOT_TOKEN = 6148802631:AAF4snzwwOuAZ4rEpZ_Dj7rCvoBUjjy5f1Y
SESSION = BQAJkbkA62zB3222ylcSm_zI_RagIsAQUqCT93WMUdKWeFLbpwV10kddFSqb8DCLkflSePWeNMB3YwkqNx_TSspdchCxcs058Jwjun8RD5klC4htSF6F0S2nkd5N7OGXoDW6jW3ETzzzz99v_jIdue30VV87QalqI7Iuqj8ECF78gbvQjZG4J56uKhSQa3chMqgzI4v2IfIOevh7FVBDsz6UJInU0ECcTX_onh5socGURSkHD4lYSQkLO2HDgudz6X9gOzSgLUKsuV8xqTjJd351YwZWawaVEij7tU762KeKd-ZoZdJCshE1CVafg7viwLl-EGg0xnLgT0BR_BsdY3FDAAAAAV_-LKkA
FORCESUB = FYBRARE
AUTH = 5770088662


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
