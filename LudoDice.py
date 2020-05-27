"""
TinyurlBoT
"""

import logging
import pyshorteners
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '1099402493:AAGVZgwWlgUOX763ALt2qfIIwxmtmq7gGDc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
s = pyshorteners.Shortener()
welcome_msg = "👋 Hi there i'm Tinyurl Bot !!\n🤖 This bot can short any link\n🔥 Fastest url shortener Bot\n🔗 Just send me your link"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.answer(welcome_msg)

@dp.message_handler()
async def echo(message: types.Message):
	await message.answer('Here Is Your Shortened Url👇\n\n' + (s.tinyurl.short(message.text)))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
