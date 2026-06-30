from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def sent_detector(): 
    # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract emotions and dominant emotion from the response 
    anger_score = response['anger'] 
    disgust_score = response['disgust'] 
    fear_score = response['fear'] 
    joy_score = response['joy'] 
    sadness_score = response['sadness'] 
    dominant_emotion_name = response['dominant_emotion']

    # Check if the one of variables assigned from response is None, indicating an error or invalid input
    if any(emotion is None for emotion in (
        anger_score,
        disgust_score,
        fear_score,
        joy_score,
        sadness_score,
        dominant_emotion_name
    )):
        return "Invalid text! Please try again!"
    else:
        # Return a formatted string with the emotion scores and the dominant emotion 
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion_name)

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)