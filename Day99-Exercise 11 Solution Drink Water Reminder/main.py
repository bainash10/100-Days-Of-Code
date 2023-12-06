import ctypes
import pyttsx3
import time
# pyttsx3 library for text-to-speech and the ctypes library for displaying alerts. 
# can also use "windows task scheduler" for scheduling the reminder

REPEAT_INTERVAL=5

# Function to display an alert on Windows
def display_alert(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

# Function to speak a given text
def speak(text):
    #The speak function initializes the pyttsx3 engine, sets the text to be spoken, and then runs the engine to speak the text. 

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the text to be spoken
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Main program
while True:
    # Set the message
    message = "Hey Harry, drink water"

    # Display an alert
    display_alert("Hey Harry", message)

    # Speak the message
    speak(message)

    time.sleep(REPEAT_INTERVAL)
