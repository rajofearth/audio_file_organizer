import os
import re
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack

def prompt_customization():
    # Ask the user for the desired folder structure
    folder_structure = input("Enter desired folder structure (e.g., artist/album, genre/artist/album): ")
    return folder_structure

def extract_metadata(audio):
    # Extract artist, album, and genre from audio file metadata
    if 'TPE1' in audio:
        artist = audio['TPE1'].text[0]
    else:
        artist = "Unknown Artist"
    if 'TALB' in audio:
        album = audio['TALB'].text[0]
    else:
        album = "Unknown Album"
    if 'TCON' in audio:
        genre = audio['TCON'].text[0]
    else:
        genre = "Unknown Genre"
    return artist, album, genre

def sanitize_directory_name(name):
    # Remove special characters using regular expression
    name = re.sub(r'[^\w\s-]', '', name)
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Limit the maximum length of directory names
    max_length = 255
    if len(name) > max_length:
        name = name[:max_length]
    return name

def organize_audio_custom():
    audio_directory = input("Enter the path to the folder containing audio files: ")
    folder_structure = prompt_customization()

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
                elif file_name.endswith('.flac'):
                    audio = FLAC(file_path)
                elif file_name.endswith('.wav') or file_name.endswith('.wv'):
                    audio = WavPack(file_path)
                
                # Extract metadata
                artist, album, genre = extract_metadata(audio)

                # Sanitize directory names
                artist = sanitize_directory_name(artist)
                album = sanitize_directory_name(album)
                genre = sanitize_directory_name(genre)
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                continue
            
            # Split the folder structure into parts
            structure_parts = folder_structure.split('/')
            
            # Create directory structure based on user input
            current_path = audio_directory
            for part in structure_parts:
                if part.lower() == 'artist':
                    current_path = os.path.join(current_path, artist)
                elif part.lower() == 'album':
                    current_path = os.path.join(current_path, album)
                elif part.lower() == 'genre':
                    current_path = os.path.join(current_path, genre)
                if not os.path.exists(current_path):
                    os.makedirs(current_path)

           # Move file to the final directory
            new_file_path = os.path.join(current_path, file_name)
            os.rename(file_path, new_file_path)
            print(f"Moved {file_name} to {current_path}")
        else:
            print(f"Ignored {file_name}: Not an audio file")

    print("Organizing complete!")

# Call the function to start organizing
organize_audio_custom()
