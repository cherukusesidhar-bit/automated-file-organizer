"""
Automated File Organizer
Organizes files in a selected folder by file extension.

Usage:
    python main.py
    python main.py "C:/Users/YourName/Downloads"
"""

from pathlib import Path
import shutil
import sys

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".wmv"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Python Files": {".py", ".ipynb"},
    "Code": {".c", ".cpp", ".java", ".js", ".html", ".css", ".json"},
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        print(f"Error: '{folder}' is not a valid folder.")
        return

    moved = 0
    skipped = 0

    for item in folder.iterdir():
        if not item.is_file() or item.name == Path(__file__).name:
            continue

        category = get_category(item.suffix)
        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)
        destination = destination_folder / item.name

        # Avoid overwriting a file with the same name.
        if destination.exists():
            print(f"Skipped (already exists): {item.name}")
            skipped += 1
            continue

        try:
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/")
            moved += 1
        except OSError as error:
            print(f"Could not move {item.name}: {error}")
            skipped += 1

    print("\nOrganization completed!")
    print(f"Files moved: {moved}")
    print(f"Files skipped: {skipped}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    else:
        target_folder = input("Enter the folder path to organize: ").strip().strip('"')

    organize_folder(target_folder)
