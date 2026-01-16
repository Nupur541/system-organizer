import os
import shutil
import sys

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist.")
        return

    files = os.listdir(folder_path)

    if not files:
        print("📂 Folder is empty.")
        return

    for file in files:
        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)

                try:
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved {file} → {folder}/")
                except PermissionError:
                    print(f"⚠️ Skipped {file} (file is currently in use)")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved {file} → Others/")
            except PermissionError:
                print(f"⚠️ Skipped {file} (file is currently in use)")

    print("\n✅ Folder organized successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
    else:
        organize_folder(sys.argv[1])
