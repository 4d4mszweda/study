import os
import shutil

def sort_files(source_folder):
    # Ścieżki do nowych folderów
    dogs_folder = os.path.join(source_folder, 'dogs')
    cats_folder = os.path.join(source_folder, 'cats')

    # Tworzenie nowych folderów, jeśli nie istnieją
    os.makedirs(dogs_folder, exist_ok=True)
    os.makedirs(cats_folder, exist_ok=True)

    # Iteracja przez pliki w katalogu źródłowym
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Sprawdzenie, czy jest to plik
        if os.path.isfile(file_path):
            # Przenoszenie plików do odpowiednich folderów
            if 'dog' in filename.lower():
                shutil.move(file_path, os.path.join(dogs_folder, filename))
            elif 'cat' in filename.lower():
                shutil.move(file_path, os.path.join(cats_folder, filename))

if __name__ == "__main__":
    source_folder = './dogs-cats-mini'  # Zmień na ścieżkę do swojego katalogu
    sort_files(source_folder)