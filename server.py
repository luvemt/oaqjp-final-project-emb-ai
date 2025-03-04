"""
Emotion detector server

"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")



@app.route("/")
def render_index():
    """
    Renders index.html
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def get_emotional_detector():
    """
    Calls emotional detector and returns result on given input text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    detector_response = emotion_detector(text_to_analyze)

    if not detector_response['dominant_emotion']:
        return "Invalid text! Please try again!."
    emotions = "For the given statement, the response is "
    for index, key in enumerate(detector_response):
        if index > len(detector_response) - 2:
            break

        emotions = emotions + "'" + str(key)+  "'" + ": "+str(detector_response[key])
        if index == len(detector_response) - 3:
            emotions = emotions + " and "
        elif index == len(detector_response)-2:
            emotions = emotions + "."

        else:
            emotions = emotions + ", "
    output = emotions + " The dominant emotion is "\
     + str(detector_response['dominant_emotion']) + "."

    return output

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
