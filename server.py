"""
Executing this function initiates the application of emotion
detector to be executed over the Flask channel and deployed on
localhost:5000.
"""

#importing libraries needed
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#calling the app
app = Flask("Emotion Detector")

#Initiate the flask app
@app.route("/emotionDetector")
def sent_analyzer():
    """
    Retrieves text from request arguments and analyzes its emotion.
    Returns:
    str: result and dominant_emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant_emotion from the response
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion != "None":

        # Remove 'dominant_emotion'
        response.pop('dominant_emotion', None)

        # Format dictionary as a string without {}
        formatted_result = ", ".join(f"'{key}': {value}" for key, value in response.items())

        #Return a formatted string with the the formatted
        #dictionary of emotions and the dominant emotion
        return (
        f"For the given statement, the system response is {formatted_result}. "
        f"The dominant emotion is {dominant_emotion}."
        )

    # Return a invalid response message
    return "Invalid text! Please try again!."

#decorator
@app.route("/")
#method that renders the index.html
def render_index_page():
    """
    Renders the index page.
    Returns:
        Template: Renders index.html.
    """
    return render_template('index.html')

#calling host and port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
