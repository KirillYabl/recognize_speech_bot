from telegram import ext
import dotenv

import logging
import os


def start(bot, update):
    """Just hello message for /start command.
    :param bot: tg bot object
    :param update: event with update tg object
    """
    bot.send_message(chat_id=update.message.chat_id, text='Здравствуйте')


def echo(bot, update):
    """Send echo message.
    :param bot: tg bot object
    :param update: event with update tg object
    """
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s  %(name)s  %(levelname)s  %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    dotenv.load_dotenv()
    TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')

    REQUEST_KWARGS = {
        # "USERNAME:PASSWORD@" is optional, if you need authentication:
        'proxy_url': 'https://45.163.161.58:8080',
    }

    # create updater. More highlevel interface of Bot
    updater = ext.Updater(token=TG_BOT_TOKEN, request_kwargs=REQUEST_KWARGS)

    # add handlers
    updater.dispatcher.add_handler(ext.CommandHandler('start', start))
    updater.dispatcher.add_handler(ext.MessageHandler(ext.Filters.text, echo))

    updater.start_polling()
