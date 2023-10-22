import speech_recognition as sr
import openai

# Set up your OpenAI API credentials
openai.api_key = "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"

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Speak something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        temperature=0.7,
        stop=None
    )
    return response.choices[0].text.strip()

# Main program loop
while True:
    user_input = recognize_speech()
    if user_input:
        response = generate_response(user_input)
        print("AI: " + response)
    else:
        print("Please try again.")
