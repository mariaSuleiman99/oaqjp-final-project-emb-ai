"""
server.py

This module defines a Flask web application for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Web App")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Handle emotion detection request.
    Retrieves the text input from the request, calls the emotion_detector function,
    and returns a formatted response string with emotion scores and dominant emotion.
    Returns:
        str: Formatted system response including dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion')
    # Handle blank input or error case
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400
    # Format the output as required
    return (
        f"For the given statement, the system response is "
        f"'anger': {response.get('anger', 0)}, "
        f"'disgust': {response.get('disgust', 0)}, "
        f"'fear': {response.get('fear', 0)}, "
        f"'joy': {response.get('joy', 0)}, "
        f"'sadness': {response.get('sadness', 0)}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index page of the web application.
    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
