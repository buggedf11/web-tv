import gtts  # google text to speech
import speech_recognition as sr
import re
import os

# Function to convert text to speech
def speak(text):
    tts = gtts.gTTS(text)
    tts.save("output.mp3")
    os.system("start output.mp3")

# Function to handle voice commands
def handle_command(command):
    if command.lower() == "stop":
        print("Exiting program...")
        exit()
    elif command.lower() == "repeat":
        if last_text:
            print("Repeating last recognized text:", last_text)
            speak(last_text)
        else:
            print("No text to repeat")
    else:
        # Check if the command is an arithmetic expression
        match = re.match(r'(\d+)\s*([\+\-\*/])\s*(\d+)', command)
        if match:
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            
            response = f"{num1} {operator} {num2} = {result}"
            print(response)
            speak(response)
        else:
            print("Command not recognized")

# Voice detection
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        last_text = text  # Store last recognized text

        # Handle voice commands
        handle_command(text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
