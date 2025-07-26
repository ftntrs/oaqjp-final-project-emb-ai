from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# curl localhost:5000/emotionDetector?statement='I love my life'
# curl localhost:5000/emotionDetector?statement="I love my life"
# curl 'localhost:5000/emotionDetector?statement=I love my life'
@app.route("/emotionDetector")
def emotion_detector():
    statement = request.args.get('statement')
    response = emotion_detector(statement)
    # return "给定的文本已被识别为 {}，得分为 {}.".format(label.split('_')[1], score)
    return f"""For the given statement, the system response is 
    'anger': {response['anger']}, 
    'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 
    'joy': {response['joy']} and 'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}."""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

