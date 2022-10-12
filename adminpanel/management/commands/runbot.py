from django.core.management import BaseCommand
from aiogram import executor
from telebot import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        executor.start_polling(bot.dp, skip_updates=False)
