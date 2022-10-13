from telegram import Update
from telegram.ext import CallbackContext
from adminpanel.models import Profile, Message


def do_echo(update: Update, context: CallbackContext):
    _add_message_to_db(update)
    update.message.reply_text(update.message.text)
    return update


def _add_message_to_db(update):
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
