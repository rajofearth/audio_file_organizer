
# MP3 Organizer

This Python script helps organize your MP3 files by artist and album, creating a tidy directory structure for your music library.
Created by [Rajofearth](https://github.com/rajofearth) with the help of ChatGPT 3.5

## Getting Started

### Prerequisites
- Python 3.x
- Mutagen library (install using `pip install mutagen`)

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/mp3_organizer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd mp3_organizer
   ```

3. Run the script:
   ```bash
   python3 mp3orga.py
   ```

### Usage
1. Run the script `mp3orga.py`.
2. Scrpt will ask User to for Folder of mp3 Files, for example
   $ python3 mp3orga1.py
   Enter the path to the folder containing MP3 files:
4. The script will organize your MP3 files into folders based on artist and album.

#### Folder Structure
```markdown
.
└── mp3_files
    ├── Artist1
    │   ├── Album1
    │   │   ├── song1.mp3
    │   │   ├── song2.mp3
    │   │   └── ...
    ├── Artist2
    │   ├── Album1
    │   │   ├── song1.mp3
    │   │   ├── song2.mp3
    │   │   └── ...
    │   ├── Album2
    │   │   ├── song1.mp3
    │   │   ├── song2.mp3
    │   │   └── ...
    │   └── ...
    └── ...
```

## Note
If you want to change the path where your songs are located, you can modify the `mp3_directory` variable in the `mp3orga.py` script to point to your desired folder location.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Made with the help of ChatGPT 3.5 🤖
---
