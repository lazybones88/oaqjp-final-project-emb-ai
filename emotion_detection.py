import requests


def emotion_detector(text_to_analyze):
    """
    Run emotion detection using the Watson NLP Emotion Predict API.
    Returns the text attribute of the response object.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)
    return response.text
