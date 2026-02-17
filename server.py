"""
Flask server for the Emotion Detection web app.
Serves the UI and the /emotionDetector API used by the frontend.
"""
from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the main page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    GET /emotionDetector?textToAnalyze=<text>
    Returns formatted emotion analysis result for the frontend.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    try:
        result = emotion_detector(text_to_analyze.strip())
    except Exception as e:
        return f"Error analyzing text: {e}"

    # Error handling: when dominant_emotion is None (e.g. blank entry, status_code 400)
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Format the result as specified: 'anger': x, 'disgust': x, 'fear': x, 'joy': x and 'sadness': x. The dominant emotion is X.
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
