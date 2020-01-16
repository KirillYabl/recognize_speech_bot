import dialogflow_v2 as dialogflow
import dotenv

import logging
import json
import os


def read_json(fname):
    """Read JSON file.
    :param fname: str, path to file
    :return: dict, json
    """
    with open(fname, encoding='utf8') as f:
        result = json.load(f)
    return result


def build_intent_for_api(intent_name, questions, answer):
    """Build structure of intent for dialogflow API.
    :param intent_name: str, name of intent
    :param questions: iterable, iterable of questions
    :param answer: str, answer to question
    :return: dict, intent for api
    """
    intent = {'display_name': intent_name,
              'messages': [{'text': {'text': [answer]}}],
              'training_phrases': []}

    for question in questions:
        phrase = {'parts': [{'text': question}]}
        intent['training_phrases'].append(phrase)

    return intent


def create_intent(intent, project_id, language_code):
    """Create intent in dialogflow
    :param intent: dict, intent for api
    :param project_id: str, secret project id
    :param language_code: event with update tg object
    :return:
    """
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)
    response = client.create_intent(parent, intent, language_code=language_code)

    return response


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s  %(name)s  %(levelname)s  %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    dotenv.load_dotenv()
    DF_PROJECT_ID = os.getenv('DF_PROJECT_ID')
    DF_CREDENTIALS_PATH = os.getenv('DF_CREDENTIALS_PATH')
    DF_LANGUAGE_CODE = os.getenv('DF_LANGUAGE_CODE')

    # For deploy local
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = DF_CREDENTIALS_PATH

    training_intents = read_json('training_intents.json')
    logger.info('readed training intents')

    logger.info('start create intents')
    for intent_name, intent_info in training_intents.items():
        questions = intent_info['questions']
        answer = intent_info['answer']

        intent = build_intent_for_api(intent_name, questions, answer)
        response = create_intent(intent, project_id=DF_PROJECT_ID, language_code=DF_LANGUAGE_CODE)
        logger.info('intent {} created'.format(intent_name))
