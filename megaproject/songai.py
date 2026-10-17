import pyttsx3
import speech_recognition as sr
from pytube import Search, YouTube
import os

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
        print("Listening for the song name...")
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

def search_and_play_song(song_name):
    """
    Search for a song on YouTube, download its audio, and play it.
    :param song_name: The name of the song to search for.
    """
    speak(f"Searching for {song_name} on YouTube.")
    print(f"Searching for {song_name} on YouTube...")

    try:
        # Search for the song on YouTube
        search = Search(song_name)
        video = search.results[0]  # Get the first result
        video_url = video.watch_url
        speak(f"found{video.title}.fuck you i am trying to reach out the code.")

        speak(f"Found {video.title}. Downloading now.")
        print(f"Found: {video.title}\nDownloading...")

        # Download the audio of the video
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = audio_stream.download()

        # Rename to .mp3 for compatibility
        base, ext = os.path.splitext(output_path)
        audio_file = f"{base}.mp3"
        os.rename(output_path, audio_file)

        # Play the audio
        speak(f"Playing {video.title} now.")
        print(f"Playing: {video.title}")
        os.system(f"start {audio_file}" if os.name == "nt" else f"open {audio_file}")

    except Exception as e:
        speak("Sorry, I couldn't complete the task.")
        print(f"An error occurred: {e}")

# Main function to handle the workflow
def main():
    speak("Hello! I am Jarvis. Tell me the name of the song you want me to play.")
    while True:
        song_name = take_command()
        if song_name:
            if "exit" in song_name or "quit" in song_name:
                speak("Goodbye! Have a great day.")
                break
            else:
                search_and_play_song(song_name)

# Run the program
if __name__ == "__main__":
    main()
