# Telegram Bot with Django Template
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django?color=green)
![Django Version](https://img.shields.io/badge/Django-4.1.2-green)
![python-telegram-bot Version](https://img.shields.io/badge/python--telegram--bot-13.14-green)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mmbogdanov/telegram-bot-with-django-template)
![GitHub issues](https://img.shields.io/github/issues/mmbogdanov/telegram-bot-with-django-template)
## Description
A template for creating bots with an admin panel. The bot records user data and messages. Based on python-telegram-bot and django.
## Installing
Clone this repo:
```console
git clone https://github.com/mmbogdanov/telegram-bot-with-django-template.git
```
Install requirements:
```console
mkvirtualenv --python=python3.10 venv
workon venv
pip install -r requirements.txt
```
Make migrations:
```console
workon venv
python manage.py makemigrations
python manage.py migrate
```
Create superuser:
```console
workon venv
python manage.py createsuperuser
```
Create config.env with token:
```
TG_TOKEN=YOUR_TOKEN
PORT=80
WEBHOOK_URL=https://example.com/
```
Run admin panel:
```console
workon venv
python manage.py runserver
```
Run bot in Long Polling mode:
```console
workon venv
python manage.py runbot --polling
```
or run bot in Webhook mode:
```console
workon venv
python manage.py runbot --webhook
```
## Usage
Open admin panel at http://127.0.0.1:8000/admin

You can view users and the messages they've sent.
### What's next?
Then you can upgrade the bot and add new models to the admin panel.
## Contributing
Contributions of all sizes are welcome. You can also help by [reporting bugs or feature requests](https://github.com/mmbogdanov/telegram-bot-with-django-template/issues).

