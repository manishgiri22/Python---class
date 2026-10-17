from pytube import YouTube
import os

# Dictionary containing song names and YouTube URLs
songs = {
    "song1": "https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
    "song2": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "song3": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Rickroll :)
}

def download_and_play(song_name):
    """
    Download and play a YouTube video as audio for the given song name.
    :param song_name: Name of the song as in the dictionary.
    """
    if song_name not in songs:
        print(f"Error: {song_name} not found in the song list.")
        return

    url = songs[song_name]
    print(f"Downloading {song_name} from {url}...")

    try:
        # Create YouTube object and download audio
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = audio_stream.download()

        # Rename downloaded file to ensure compatibility with OS
        base, ext = os.path.splitext(output_path)
        audio_file = f"{base}.mp3"
        os.rename(output_path, audio_file)

        # Play the audio
        print(f"Playing {song_name}...")
        os.system(f"start {audio_file}" if os.name == "nt" else f"open {audio_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
