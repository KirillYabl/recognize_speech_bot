import dialogflow_v2 as dialogflow

import logging


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation.
    :param project_id: str, secret project id
    :param session_id: str or int, some number
    :param texts: iterable, elements of iterable are input messages
    :param language_code: event with update tg object
    :return: str, answer from dialogflow or unknown_answer if dialogflow dont know texts
    """
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    logger = logging.getLogger(__name__ + 'detect_intent_texts')
    logger.debug('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(session=session, query_input=query_input)

        logger.debug('Query text: {}'.format(response.query_result.query_text))

        detected_intent = response.query_result.intent.display_name
        confidence = response.query_result.intent_detection_confidence
        logger.debug('Detected intent: {} (confidence: {})'.format(detected_intent, confidence))

        fulfillment_text = response.query_result.fulfillment_text
        logger.debug('Fulfillment text: {}'.format(fulfillment_text))

        if response.query_result.intent.is_fallback == True:
            return ''

        return fulfillment_text
