import logging
import os

from telegram.ext import Updater, MessageHandler, Filters
from dotenv import load_dotenv
from setting.settings import BASE_DIR
from telebot.handlers import do_echo

logging.basicConfig(level=logging.INFO)

load_dotenv(BASE_DIR / 'config.env')


def _add_handlers(updater: Updater):
    updater.dispatcher.add_handler(MessageHandler(Filters.text, do_echo))


def start_polling():
    updater = Updater(os.getenv('TG_TOKEN'), use_context=True)
    _add_handlers(updater)
    updater.start_polling()
    updater.idle()


def start_webhook():
    updater = Updater(os.getenv('TG_TOKEN'), use_context=True)
    _add_handlers(updater)
    updater.start_webhook(listen="0.0.0.0",
                          port=os.environ.get('PORT', '8443'),
                          url_path=os.getenv('TG_TOKEN'),
                          webhook_url=os.getenv('WEBHOOK_URL') + os.getenv('TG_TOKEN'))
    updater.idle()
