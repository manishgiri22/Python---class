import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

import music

def main():
    print("Available Songs:")
    for song in music.songs:
        print(f"- {song}")

    while True:
        user_input = input("Enter the song name to play (or type 'exit' to quit): ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input in music.songs:
            music.download_and_play(user_input)
        else:
            print("Song not found. Please try again.")

if __name__ == "__main__":
    main()


# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Set speaking speed
engine.setProperty("volume", 1.0)  # Set volume level

def speak(text):
    """
    Convert text to speech.
    :param text: The text to be spoken.
    """
    engine.say(text)
    engine.runAndWait()

def take_command():
    """
    Capture microphone input and return the recognized text.
    :return: Recognized command as a string.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Unable to connect to the speech recognition service.")
            return None

def perform_task(command):
    """
    Perform a specific task based on the user's command.
    :param command: User's voice input.
    """
    if "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}.")
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "play music" in command:
        music_dir = "C:/Users/YourUsername/Music"  # Replace with your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music.")
        else:
            speak("Your music folder is empty.")
    elif "date today" in command:
        today_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is {today_date}.")
    elif "quit" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        exit(0)
    else:
        speak("I'm not sure how to help with that. Please try asking something else.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        command = take_command()
        if command:
            perform_task(command)
