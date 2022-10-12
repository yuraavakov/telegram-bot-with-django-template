from django.core.management import BaseCommand
from telebot import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.run()
