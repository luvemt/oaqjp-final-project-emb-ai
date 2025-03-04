import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers = header, json = input_text)
    if response.status_code == 400:
        emotions ={
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = ''
    max_score = 0
    for key, value in emotions.items():
        if value > max_score:
            max_score = value
            dominant_emotion = key

    emotions['dominant_emotion'] = dominant_emotion
    return emotions

