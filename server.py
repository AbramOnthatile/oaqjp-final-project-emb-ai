"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template, request

from emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main emotion detection page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text provided by the user and return the emotion results."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
