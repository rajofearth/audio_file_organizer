import os
from mutagen.mp3 import MP3

def organize_mp3_by_artist_and_album():
    mp3_directory = input("Enter the path to the folder containing MP3 files: ")

    # Check if the directory exists
    if not os.path.isdir(mp3_directory):
        print("Invalid directory path. Please enter a valid directory path.")
        return

    # Iterate through each file in the directory
    for file_name in os.listdir(mp3_directory):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(mp3_directory, file_name)
            
            # Extract metadata
            try:
                audio = MP3(file_path)
                artist = audio['TPE1'].text[0]
                album = audio['TALB'].text[0]
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                continue
            
            # Create directory if not exists
            artist_directory = os.path.join(mp3_directory, artist)
            if not os.path.exists(artist_directory):
                os.makedirs(artist_directory)
            album_directory = os.path.join(artist_directory, album)
            if not os.path.exists(album_directory):
                os.makedirs(album_directory)
            
            # Move file to appropriate directory
            new_file_path = os.path.join(album_directory, file_name)
            os.rename(file_path, new_file_path)
            print(f"Moved {file_name} to {artist}/{album}")
    
    print("Organizing complete!")

# Call the function to start organizing
organize_mp3_by_artist_and_album()
