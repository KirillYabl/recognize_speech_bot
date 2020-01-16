from telegram import ext
import dotenv

from common_functions import detect_intent_texts

import logging
import os


def start(bot, update):
    """Just hello message for /start command.
    :param bot: tg bot object
    :param update: event with update tg object
    :param project_id: str, secret project id
    :param session_id: str or int, some number
    :param language_code: event with update tg object
    """
    bot.send_message(chat_id=update.message.chat_id, text='Здравствуйте')


def echo(bot, update):
    """Send echo message.
    :param bot: tg bot object
    :param update: event with update tg object
    """
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def dialog_flow_answer(bot, update, project_id, session_id, language_code):
    """Send message with using dialogflow.
    :param bot: tg bot object
    :param update: event with update tg object
    :param project_id: str, secret project id
    :param session_id: str or int, some number
    :param language_code: event with update tg object
    """
    answer = detect_intent_texts(project_id, session_id, [update.message.text], language_code)
    bot.send_message(chat_id=update.message.chat_id, text=answer)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s  %(name)s  %(levelname)s  %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    dotenv.load_dotenv()
    TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
    DF_PROJECT_ID = os.getenv('DF_PROJECT_ID')
    DF_CREDENTIALS_PATH = os.getenv('DF_CREDENTIALS_PATH')
    DF_SESSION_ID = os.getenv('DF_SESSION_ID')
    DF_LANGUAGE_CODE = os.getenv('DF_LANGUAGE_CODE')

    # For deploy local
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = DF_CREDENTIALS_PATH

    REQUEST_KWARGS = {}
    # If you are from mother Russia
    # REQUEST_KWARGS['proxy_url'] = 'https://PROXY_IP:PROXY_PORT'

    # create updater. More highlevel interface of Bot
    updater = ext.Updater(token=TG_BOT_TOKEN, request_kwargs=REQUEST_KWARGS)

    # add handlers
    msg_handler = lambda bot, update: dialog_flow_answer(bot, update, DF_PROJECT_ID, DF_SESSION_ID, DF_LANGUAGE_CODE)

    updater.dispatcher.add_handler(ext.CommandHandler('start', start))
    updater.dispatcher.add_handler(ext.MessageHandler(ext.Filters.text, msg_handler))
    while True:
        try:
            updater.start_polling()
        except Exception:
            logger.exception('Critical error in ')
