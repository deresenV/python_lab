import tkinter
import hashlib
import os
import threading
from tkinter import filedialog, ttk
from collections import defaultdict

file_path = None

def create_window():
    root = tkinter.Tk()
    root.update_idletasks()
    width, height = 900, 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")
    return root


def upload_file():
    global file_path
    file_path = filedialog.askdirectory(title="Select Profile Picture")
    ttk.Label(root, text=f"Выбрана директория:{file_path}").pack(anchor=tkinter.CENTER)
    ttk.Button(root, text="Начать поиск", command=start_scan).pack(anchor=tkinter.CENTER)

def start_scan():
    """Запуск алгоритма сортировки файлов и поиска дюпнутых"""
    filter_with_size_scan()


def filter_with_size_scan():
    """Сканирует по размеру и закидывает в словарь в конечном итоге если у лишь 1 файла есть такой размер то у файла не может быть дубликатов и мы его удаляем
    :return: array путей до файлов с одинаковым весом
    """
    global file_path
    size_dict = defaultdict(list)

    for root, dirs, files in os.walk(file_path):  # Рекурсивный обход папок
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)  # Получаем размер файла
                size_dict[file_size].append(file_path)  # Группируем файлы по размеру
            except (PermissionError, FileNotFoundError):
                continue  # Игнорируем файлы, к которым нет доступа

    # Убираем файлы с уникальным размером
    return {size: paths for size, paths in size_dict.items() if len(paths) > 1}



def fast_byte_scan():
    pass


def hash_scan():
    pass

def end_byte_scan():
    pass


root = create_window()

open_button = ttk.Button(root, text="Выбрать директорию", command=upload_file)
open_button.pack(pady=10)

root.mainloop()
