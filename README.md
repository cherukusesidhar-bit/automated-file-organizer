# Automated File Organizer

A Python command-line application that automatically organizes files into folders based on their file extensions.

## Features
- Sorts images, documents, videos, audio, archives, Python files and code files.
- Places unrecognized file types in an `Others` folder.
- Creates category folders automatically.
- Avoids overwriting files when a destination filename already exists.
- Displays a summary of moved and skipped files.

## Requirements
- Python 3.8 or later
- No external packages required

## How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

4. Enter the full path of the folder you want to organize.

You can also pass the folder path directly:

```bash
python main.py "C:/Users/YourName/Downloads"
```

## Safety Note
Test the program first on a temporary folder containing copies of sample files. The program moves files into category folders; it does not delete them.

## Technologies Used
- Python
- pathlib
- shutil
- sys

## Author
Sesidhar
