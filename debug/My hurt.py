from flask import Flask, render_template
import speech_recognition as sr
from gtts import gTTS
import os
import openai

# Initialize the Flask app
app = Flask(__name__)

# Initialize the recognizer and last question variables
r = sr.Recognizer()
first_question = ""

# Initialize the OpenAI API key
openai.api_key = ""

# Define a function to listen for speech and return the text
def recognize_speech():
    global first_question  # Access the global variable

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        
        if "first question" in text:
            print("The first question asked was:", first_question)
            return first_question
        
        first_question = text  # Update the last question variable
        return text
    
    except sr.UnknownValueError:
        print("Sorry, could not understand your speech")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Define a function to call the OpenAI API and generate a response to a given prompt
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=600,
        n=1,
        stop=None,
        timeout=10,
    )
    return response.choices[0].text.strip()

# Define a route to render the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define a route to handle speech recognition
@app.route("/speech-recognition")
def speech_recognition():
    text = recognize_speech()
    prompt = "The user said: {}\nAI:".format(text)
    response = generate_response(prompt)
    return response

   

if __name__ == "__main__":
    app.run(debug=True)
