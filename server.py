"""Flask web server for the EmotionDetection application.

Routes:
- / : Renders the main UI (templates/index.html).
- /emotionDetector : Returns a human-readable emotion analysis response.
"""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

APP_HOST = "0.0.0.0"
APP_PORT = 5000
INVALID_TEXT_MESSAGE = "Invalid text! Please try again!"

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Run emotion detection and return the formatted response string."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return INVALID_TEXT_MESSAGE

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


def main():
    """Start the Flask development server."""
    app.run(host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    main()
