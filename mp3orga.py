import os
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack

def organize_audio_by_artist_and_album():
    audio_directory = input("Enter the path to the folder containing audio files: ")

    # Check if the directory exists
    if not os.path.isdir(audio_directory):
        print("Invalid directory path. Please enter a valid directory path.")
        return

    # Iterate through each file in the directory
    for file_name in os.listdir(audio_directory):
        file_path = os.path.join(audio_directory, file_name)
        
        # Check if the file is an audio file
        if file_name.endswith(('.mp3', '.flac', '.wav', '.wv')):
            try:
                if file_name.endswith('.mp3'):
                    audio = MP3(file_path)
                    artist = audio['TPE1'].text[0]
                    album = audio['TALB'].text[0]
                elif file_name.endswith('.flac'):
                    audio = FLAC(file_path)
                    artist = audio['artist'][0]
                    album = audio['album'][0]
                elif file_name.endswith('.wav') or file_name.endswith('.wv'):
                    audio = WavPack(file_path)
                    artist = audio['artist'][0]
                    album = audio['album'][0]
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                continue
            
            # Create directory if not exists
            artist_directory = os.path.join(audio_directory, artist)
            if not os.path.exists(artist_directory):
                os.makedirs(artist_directory)
            album_directory = os.path.join(artist_directory, album)
            if not os.path.exists(album_directory):
                os.makedirs(album_directory)
            
            # Move file to appropriate directory
            new_file_path = os.path.join(album_directory, file_name)
            os.rename(file_path, new_file_path)
            print(f"Moved {file_name} to {artist}/{album}")
        else:
            print(f"Ignored {file_name}: Not an audio file")

    print("Organizing complete!")

# Call the function to start organizing
organize_audio_by_artist_and_album()
