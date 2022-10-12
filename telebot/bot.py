import logging
import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from setting.settings import BASE_DIR


logging.basicConfig(level=logging.INFO)

load_dotenv(BASE_DIR / 'config.env')

bot = Bot(token=os.getenv('TG_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
