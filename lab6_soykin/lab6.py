import tkinter
import os
from tkinter import *
from tkinter import ttk, filedialog
from collections import defaultdict
import hashlib

file_path = None
dupls_listbox = None
start_button = None
delete_button = None


def create_window():
    global dupls_listbox, start_button, delete_button
    root = tkinter.Tk()
    root.update_idletasks()
    width, height = 900, 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")
    root.title("fduples")
    icon = PhotoImage(file="ico/logo.png")
    root.iconphoto(False, icon)

    ttk.Label(root, text="Выберите директорию для поиска дубликатов").pack()

    open_button = ttk.Button(root, text="Выбрать директорию", command=upload_file)
    open_button.pack(pady=10)

    start_button = ttk.Button(root, text="Начать поиск", command=start_scan)
    start_button.pack(pady=5)
    start_button.pack_forget()

    delete_button = ttk.Button(root, text="Удалить выбранные", command=delete_selected_files)
    delete_button.pack(pady=5)
    delete_button.pack_forget()

    dupls_listbox = Listbox(root, selectmode=MULTIPLE)  # Multiple выбор нескольких
    dupls_listbox.place(x=50, y=200, height=200, width=800)

    return root


def delete_selected_files():
    """Удаляет файлы, которые выбрал пользователь в Listbox."""
    selected_indices = dupls_listbox.curselection()
    selected_files = [dupls_listbox.get(i) for i in selected_indices]

    for file_entry in selected_files:
        file_paths = file_entry.replace("Дубликаты: ", "").split(", ")
        for file in file_paths:
            try:
                os.remove(file)
                print(f"Удалён файл: {file}")
            except Exception as e:
                print(f"Ошибка удаления {file}: {e}")

    for i in reversed(selected_indices):
        dupls_listbox.delete(i)


def upload_file():
    '''Загрузка директории'''
    global file_path
    file_path = filedialog.askdirectory(title="Выберите папку")
    if file_path:
        start_button.pack(pady=5)


def start_scan():
    '''Алгоритм последовательного запуска функций '''
    files_with_size = filter_with_size_scan()
    files_after_byte_scan = fast_byte_scan(files_with_size)
    files_after_full_scan = check_full_size(files_after_byte_scan)
    dupls_listbox.delete(0, END)
    has_duplicates = False
    for hash_group in files_after_full_scan.values():
        if len(hash_group) > 1:
            has_duplicates = True
            dupls_listbox.insert(END, "⚠ Одинаковые файлы:")
            for file in hash_group:
                dupls_listbox.insert(END, file)
            dupls_listbox.insert(END, "\n")

    if has_duplicates:
        delete_button.pack(pady=5)  # Показываем кнопку, если есть дубликаты
    else:
        delete_button.pack_forget()  # Скрываем, если дубликатов нет


def filter_with_size_scan():
    '''
    Скан и распределение в дикт по размеру
    :return список файлов одинакого размера
    '''
    size_dict = defaultdict(list)
    for root_dir, _, files in os.walk(file_path):
        for file in files:
            file_full_path = os.path.join(root_dir, file)
            try:
                file_size = os.path.getsize(file_full_path)
                size_dict[file_size].append(file_full_path)
            except:
                continue
    return {size: paths for size, paths in size_dict.items() if len(paths) > 1}


def fast_byte_scan(size_groups, num_bytes=1024):
    '''Проверка только первых 1024 байт файла для отсеивания
    :return дикт файлов у которых первые 1024 байт одинаковые
    '''
    def read_first_bytes(file_path):
        try:
            with open(file_path, "rb") as f:
                return f.read(num_bytes)
        except (PermissionError, FileNotFoundError):
            return None

    byte_groups = {}
    for size, files in size_groups.items():
        temp_dict = defaultdict(list)
        for file in files:
            first_bytes = read_first_bytes(file)
            if first_bytes is None:
                continue
            temp_dict[first_bytes].append(file)
        byte_groups[size] = {k: v for k, v in temp_dict.items() if len(v) > 1}
    return byte_groups


def check_full_size(byte_groups):
    '''Полная проверка файла для отсеивания
    :return дикт файлов которые полностью идентичны
    '''
    def get_file_hash(file_path):
        try:
            hasher = hashlib.sha256() # sha256 - hash file
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""): # читаем блочно для быстроты и удобства
                    hasher.update(chunk)
            return hasher.hexdigest() #full hash
        except:
            return None

    hash_groups = defaultdict(list)
    for size, file_dict in byte_groups.items():
        for files in file_dict.values():
            for file in files:
                file_hash = get_file_hash(file)
                if file_hash:
                    hash_groups[file_hash].append(file)
    return {hash: paths for hash, paths in hash_groups.items() if len(paths) > 1}


root = create_window()
root.mainloop()
