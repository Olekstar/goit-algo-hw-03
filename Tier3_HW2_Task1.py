import os
import shutil
import sys

def copy_files(src_dir, dest_dir):
    # Створення директорії призначення, якщо вона не існує
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            # Рекурсивний виклик функції для директорії
            copy_files(item_path, dest_dir)
        else:
            # Визначення розширення файлу та створення відповідної піддиректорії
            file_ext = os.path.splitext(item)[1][1:] # Вилучення розширення без крапки
            ext_dir = os.path.join(dest_dir, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            
            # Копіювання файлу в піддиректорію
            dest_file_path = os.path.join(ext_dir, item)
            try:
                shutil.copy(item_path, dest_file_path)
            except Exception as e:
                print(f"Помилка копіювання файлу {item_path} до {dest_file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до вихідної директорії.")
        sys.exit(1)
    
    src_directory = sys.argv[1]
    dest_directory = "dist" if len(sys.argv) == 2 else sys.argv[2]
    
    copy_files(src_directory, dest_directory)
