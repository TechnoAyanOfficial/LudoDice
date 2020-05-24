"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

import random 

API_TOKEN = '1269853254:AAH9C3JGFYZouqPaIfAnOefW6lq4857Ddnw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(random.choice([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
