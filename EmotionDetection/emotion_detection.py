import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(url, headers=header, json=payload)
    
    emotions_dict = json.loads(response.text)
    anger_score = emotions_dict['emotionPredictions'][0]['emotion']['anger']
    disgust_score = emotions_dict['emotionPredictions'][0]['emotion']['disgust']
    fear_score = emotions_dict['emotionPredictions'][0]['emotion']['fear']
    joy_score = emotions_dict['emotionPredictions'][0]['emotion']['joy']
    sadness_score = emotions_dict['emotionPredictions'][0]['emotion']['sadness']

    largest_emotion_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)  
    dominant_emotion_name = ''
    if largest_emotion_score == anger_score:
        dominant_emotion_name = 'anger'
    elif largest_emotion_score == disgust_score:
        dominant_emotion_name = 'disgust'        
    elif largest_emotion_score == fear_score:
        dominant_emotion_name = 'fear'        
    elif largest_emotion_score == joy_score:
        dominant_emotion_name = 'joy'        
    elif largest_emotion_score == sadness_score:
        dominant_emotion_name = 'sadness'        
    else:
        dominant_emotion_name = 'none'        
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_name
    }
