from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# curl localhost:5000/emotionDetector?statement='I love my life'
# curl localhost:5000/emotionDetector?statement="I love my life"
# curl 'localhost:5000/emotionDetector?statement=I love my life'
# curl 'http://localhost:5000/emotionDetector?statement=I%20love%20my%20life'
@app.route("/emotionDetector")
def handle_emotion():
    statement = request.args.get('statement')
    if not statement or statement.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }
    response = emotion_detector(statement)
    # return "给定的文本已被识别为 {}，得分为 {}.".format(label.split('_')[1], score)
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}.\n", 200
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

'''
theia@theiadocker-cnshirui:/home/project/final_project$ curl 'http://localhost:5000/emotionDetector?statement=I%20love%20my%20life'
<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
'''