from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.webhook import get_new_configured_app

from urllib.parse import urljoin
from aiohttp import web

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#aiofristbot


TOKEN = os.getenv('TOKEN')  # Press "Reveal Config Vars" in settings tab on Heroku and set TOKEN variable
PROJECT_NAME = os.getenv('PROJECT_NAME')  # Set it as you've set TOKEN env var

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = '/webhook/' + TOKEN
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def main_1(message: types.Message):
    await message.reply(text='бла бла бла', reply=True)


@dp.message_handler(commands=['help'])
async def send_message(message: types.Message):
    await message.reply('Привет!\nЯ - эхобот')
    await main_1(message=message)



# @dp.message_handler(content_types=['text'])
# async def main_2(message : types.Message):
#     if message.text == 'привет':
#         await bot.send_message(message.from_user.id, 'Приветики ))')

@dp.message_handler(content_types=['text'])
async def main_2(message : types.Message):
    await bot.send_message(message.from_user.id, 'Приветики ))')


# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# async def main_2(message: types.Message):
#     text = message.text
#     if text and not text.startswith('/'):
#         await message.reply(text=text)




async def on_startup(app):
    """Simple hook for aiohttp application which manages webhook"""
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)


if __name__ == '__main__':
    # Create aiohttp.web.Application with configured route for webhook path
    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    app.on_startup.append(on_startup)
    web.run_app(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  # Heroku stores port you have to listen in your app





# def main():
#     executor.start_polling(dispatcher=dp)
#
#
# if __name__ == '__main__':
#     main()