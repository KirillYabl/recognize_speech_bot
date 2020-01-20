import random
import logging
import os

from common_functions import detect_intent_texts

import dotenv
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType


def echo(event, vk_api):
    """Echo answerer
    :param event: event which discribe message
    :param vk_api: authorized session in vk
    """
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1, 1000)
    )


def dialog_flow_answerer(event, vk_api, project_id, session_id, language_code):
    """Send message with using dialogflow.
    :param event: event which discribe message
    :param vk_api: authorized session in vk
    :param project_id: str, secret project id
    :param session_id: str or int, some number
    :param language_code: event with update tg object
    """
    answer = detect_intent_texts(project_id, session_id, [event.text], language_code)
    if answer is not None:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s  %(name)s  %(levelname)s  %(message)s', level=logging.INFO)
    logger = logging.getLogger('vk_bot')

    dotenv.load_dotenv()
    VK_APP_TOKEN = os.getenv('VK_APP_TOKEN')
    DF_PROJECT_ID = os.getenv('DF_PROJECT_ID')
    DF_CREDENTIALS_PATH = os.getenv('DF_CREDENTIALS_PATH')
    DF_SESSION_ID = os.getenv('DF_SESSION_ID')
    DF_LANGUAGE_CODE = os.getenv('DF_LANGUAGE_CODE')

    # For deploy local
    if DF_CREDENTIALS_PATH is not None:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = DF_CREDENTIALS_PATH

    while True:
        try:
            vk_session = vk.VkApi(token=VK_APP_TOKEN)
            vk_api = vk_session.get_api()
            longpoll = VkLongPoll(vk_session)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    dialog_flow_answerer(event, vk_api, DF_PROJECT_ID, DF_SESSION_ID, DF_LANGUAGE_CODE)
        except Exception:
            logger.exception('Critical error in ')
