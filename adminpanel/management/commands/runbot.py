from django.core.management import BaseCommand
from telebot import bot


class Command(BaseCommand):
    help = 'Launch the bot in two modes: Long Polling or Webhook'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--polling',
            action='store_true',
            default=False,
            help='Starts polling updates from Telegram'
        )
        parser.add_argument(
            '-w',
            '--webhook',
            action='store_true',
            default=False,
            help='Starts a small http server to listen for updates via webhook'
        )

    def handle(self, *args, **options):
        if options['polling']:
            bot.start_polling()
        elif options['webhook']:
            bot.start_webhook()
        else:
            print('usage: python manage.py runbot [-h] [--polling] [--webhook]')
