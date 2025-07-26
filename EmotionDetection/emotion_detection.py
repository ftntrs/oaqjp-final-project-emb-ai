import json
import requests

'''
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
'''
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # 情感分析服务的 URL
    myobj = { "raw_document": { "text": text_to_analyze } }  # 创建一个字典，包含要分析的文本
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # 设置 API 请求所需的头信息
    response = requests.post(url, json = myobj, headers=header)  # 发送 POST 请求到 API，包含文本和头信息
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    response = {**emotion_scores, 'dominant_emotion': dominant_emotion}
    # formatted_response = json.dumps(formatted_response, indent=4)
    return response
