# emotion_detection.py

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using IBM Watson NLP EmotionPredict API.

    Parameters:
        text_to_analyze (str): The text to analyze for emotional content.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 200:
        # Convert response to JSON
        response_json = response.json()
        # Extract emotion scores
        emotion_data = response_json['emotionPredictions'][0]['emotion']
        anger = emotion_data.get('anger', 0)
        disgust = emotion_data.get('disgust', 0)
        fear = emotion_data.get('fear', 0)
        joy = emotion_data.get('joy', 0)
        sadness = emotion_data.get('sadness', 0)
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        # Return formatted dictionary
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    elif response.status_code == 400:
        # Return empty emotion values for invalid input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    else:
        # Return error message
        return {'error': 'Unexpected status code: {}'.format(response.status_code)}
