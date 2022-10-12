import logging
import os

from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram.utils.request import Request
from dotenv import load_dotenv
from adminpanel.models import Profile, Message
from setting.settings import BASE_DIR

logging.basicConfig(level=logging.INFO)

load_dotenv(BASE_DIR / 'config.env')


def do_echo(update: Update, context: CallbackContext):
    # get or add a profile to the DB
    p, _ = Profile.objects.get_or_create(
        external_id=update.message.chat_id,
        defaults={
            'name': update.message.from_user.full_name
        }
    )

    # add a message to the DB
    m = Message(
        profile=p,
        text=update.message.text
    )
    m.save()

    update.message.reply_text(update.message.text)


def run():
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0
    )
    bot = Bot(
        request=request,
        token=os.getenv('TG_TOKEN')
    )
    updater = Updater(
        bot=bot,
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(Filters.text, do_echo))
    updater.start_polling()
    updater.idle()
