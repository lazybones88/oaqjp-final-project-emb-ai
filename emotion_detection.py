import requests
import json


def emotion_detector(text_to_analyze):
    """
    Run emotion detection using the Watson NLP Emotion Predict API.
    Returns a dictionary with emotion scores and the dominant emotion.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)
    response_text = response.text

    # Convert the response text into a dictionary using json
    data = json.loads(response_text)

    # Extract emotions from the response structure
    if "emotionPredictions" in data and len(data["emotionPredictions"]) > 0:
        emotions = data["emotionPredictions"][0].get("emotion", {})
    elif "emotions" in data and isinstance(data["emotions"], list):
        emotions = {item["emotion"]: item["score"] for item in data["emotions"]}
    else:
        emotions = data

    # Extract the required emotions and their scores
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    # Find the dominant emotion (highest score)
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the required output format
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
