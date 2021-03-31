from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.webhook import get_new_configured_app
from aiogram.utils.executor import start_webhook
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from urllib.parse import urljoin
from aiohttp import web

import os
import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

#aiofristbot


# TOKEN = os.getenv('TOKEN')  # Press "Reveal Config Vars" in settings tab on Heroku and set TOKEN variable
# PROJECT_NAME = os.getenv('PROJECT_NAME')  # Set it as you've set TOKEN env var

# WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'  # Enter here your link from Heroku project settings
# WEBHOOK_URL_PATH = '/webhook/' + TOKEN
# WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)


# TOKEN = '1705182368:AAE4G_9-HB50SwVvTEJvLHEkWNLJ83kEaU4'
# APP_NAME = 'https://aio-bot-telegram-photo-phrase.herokuapp.com/'
# WEBHOOK_PATH = '/' + TOKEN
# WEBHOOK_URL = APP_NAME + TOKEN


# WEBHOOK_HOST = 'https://aio-bot-telegram-photo-phrase.herokuapp.com/'
# WEBHOOK_PATH = '/webhook/' + TOKEN
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# WEBAPP_HOST = "0.0.0.0"
# WEBAPP_PORT = 5000
#



TOKEN = '1705182368:AAE4G_9-HB50SwVvTEJvLHEkWNLJ83kEaU4'


WEBHOOK_HOST = 'https://aio-bot-telegram-photo-phrase.herokuapp.com'
WEBHOOK_PATH = f'/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.environ.get('PORT', 8443))




# WEBHOOK_HOST = 'https://aio-bot-telegram-photo-phrase.herokuapp.com'
# WEBHOOK_PATH = '/' + TOKEN
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# WEBAPP_HOST = '0.0.0.0'
# WEBAPP_PORT = os.environ.get('PORT')
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


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



async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )


# async def on_startup(dp):
#     logging.warning(
#         'Starting connection. ')
#     await bot.set_webhook(WEBHOOK_URL,drop_pending_updates=True)
#
#
# async def on_shutdown(dp):
#     logging.warning('Bye! Shutting down webhook connection')
#
#
# def main():
#     logging.basicConfig(level=logging.INFO)
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         skip_updates=True,
#         on_startup=on_startup,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )
#
#
# if __name__ == "__main__":
#     main()













# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#     logging.info(dp)
#
#
# async def on_shutdown(dp):
#     logging.info(dp)
#
#
# if __name__ == '__main__':
#     start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
#                   on_startup=on_startup, on_shutdown=on_shutdown,
#                   host=WEBAPP_HOST, port=WEBAPP_PORT)




# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#     logging.info(dp)
#
#
# async def on_shutdown(dp):
#     logging.info(dp)
#
#
# if __name__ == '__main__':
#     start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
#                   on_startup=on_startup, on_shutdown=on_shutdown,
#                   host=WEBAPP_HOST, port=WEBAPP_PORT)
#







#
# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#     # insert code here to run it after start
#
#
# async def on_shutdown(dp):
#     logging.warning('Shutting down..')
#
#     # insert code here to run it before shutdown
#
#     # Remove webhook (not acceptable in some cases)
#     await bot.delete_webhook()
#
#     # Close DB connection (if used)
#     await dp.storage.close()
#     await dp.storage.wait_closed()
#
#     logging.warning('Bye!')
#
#
# if __name__ == '__main__':
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )




#
# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#     # insert code here to run it after start
#
#
# async def on_shutdown(dp):
#     logging.warning('Shutting down..')
#
#     # insert code here to run it before shutdown
#
#     # Remove webhook (not acceptable in some cases)
#     await bot.delete_webhook()
#
#     # Close DB connection (if used)
#     await dp.storage.close()
#     await dp.storage.wait_closed()
#
#     logging.warning('Bye!')
#
#
# if __name__ == '__main__':
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )



#
# async def on_startup(app):
#     """Simple hook for aiohttp application which manages webhook"""
#     await bot.delete_webhook()
#     await bot.set_webhook(WEBHOOK_URL)
#
#
# if __name__ == '__main__':
#     # Create aiohttp.web.Application with configured route for webhook path
#     app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)
#     app.on_startup.append(on_startup)
#     web.run_app(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  # Heroku stores port you have to listen in your app
#
#
# #


# def main():
#     executor.start_polling(dispatcher=dp)
#
#
# if __name__ == '__main__':
#     main()