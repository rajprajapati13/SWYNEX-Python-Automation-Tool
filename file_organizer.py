
from pathlib import Path
import shutil

# File types and their destination folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Code": [".py", ".c", ".cpp", ".html", ".css", ".js"]
}


def organize_files(folder_path):
    """Organize files in a folder by file extension."""
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    moved_count = 0

    for item in folder.iterdir():
        # Skip folders and this script itself
        if not item.is_file() or item.name == Path(__file__).name:
            continue

        destination_name = "Others"

        for category, extensions in FILE_TYPES.items():
            if item.suffix.lower() in extensions:
                destination_name = category
                break

        destination_folder = folder / destination_name
        destination_file = destination_folder / item.name

        try:
            destination_folder.mkdir(exist_ok=True)

            # Avoid overwriting an existing file
            if destination_file.exists():
                print(f"Skipped (already exists): {item.name}")
                continue

            shutil.move(str(item), str(destination_file))
            print(f"Moved: {item.name} -> {destination_name}/")
            moved_count += 1

        except (OSError, shutil.Error) as error:
            print(f"Could not move {item.name}: {error}")

    print(f"\nFinished! Files organized: {moved_count}")


def main():
    print("===== Python File Organizer =====")
    folder_path = input("Enter the folder path to organize: ").strip().strip('"')

    if not folder_path:
        print("Please enter a folder path.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
