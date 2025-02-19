import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

  # Check the status code before processing
    if response.status_code == 200:
        formatted_response = response.json()  # Convert response to JSON
        predictions = formatted_response.get('emotionPredictions', [])

        if predictions:
            # Extract the emotion dictionary
            emotion_scores = predictions[0].get('emotion', {})

            if emotion_scores:
                # Find the dominant emotion
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)

                # Format the output
                result = {
                    'anger': emotion_scores.get('anger', 0.0),
                    'disgust': emotion_scores.get('disgust', 0.0),
                    'fear': emotion_scores.get('fear', 0.0),
                    'joy': emotion_scores.get('joy', 0.0),
                    'sadness': emotion_scores.get('sadness', 0.0),
                    'dominant_emotion': dominant_emotion
                    }
        return result
        
    #In case of error 400
    elif response.status_code == 400:
        formatted_response = response.json()  # Convert response to JSON
        result = {
            'anger': 'None',
            'disgust': 'None',
            'fear': 'None',
            'joy': 'None',
            'sadness': 'None',
            'dominant_emotion': 'None'
            }    
    else:
        # Handle blank entries or errors
        print(f"Error: Unable to process request. Server responded with status code {response.status_code}.")

    return result  # Return the dictionary
