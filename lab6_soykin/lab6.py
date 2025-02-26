import tkinter
import os
from tkinter import *
from tkinter import ttk, filedialog
from collections import defaultdict

file_path = None
languages_listbox = None


def delete_selected_files():
    """Удаляет файлы, которые выбрал пользователь в Listbox."""
    selected_indices = languages_listbox.curselection()  # Получаем индексы выделенных файлов
    selected_files = [languages_listbox.get(i) for i in selected_indices]  # Получаем их текст

    for file_entry in selected_files:
        file_paths = file_entry.replace("Дубликаты: ", "").split(", ")  # Разбираем строку
        for file in file_paths:
            try:
                os.remove(file)
                print(f"Удалён файл: {file}")
            except Exception as e:
                print(f"Ошибка удаления {file}: {e}")

    # Обновляем Listbox
    for i in reversed(selected_indices):  # Удаляем записи из Listbox
        languages_listbox.delete(i)

# Кнопка для удаления файлов

def create_window():
    global languages_listbox
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

    languages_listbox = Listbox(root, selectmode=MULTIPLE)
    languages_listbox.place(x=50, y=200, height=200, width=800)

    return root


def upload_file():
    global file_path
    file_path = filedialog.askdirectory(title="Выберите папку")
    if file_path:
        ttk.Label(root, text=f"Выбрана директория: {file_path}").pack()
        ttk.Button(root, text="Начать поиск", command=start_scan).pack(pady=5)


def start_scan():
    """Запуск алгоритма поиска дубликатов"""
    files_with_size = filter_with_size_scan()
    files_after_byte_scan = fast_byte_scan(files_with_size)

    # Выводим дубликаты в интерфейс
    languages_listbox.delete(0, END)
    for size_group in files_after_byte_scan.values():
        for file_group in size_group.values():
            if len(file_group) > 1:
                # Добавляем строку-заголовок
                languages_listbox.insert(END, "⚠ Одинаковые файлы:")

                # Добавляем файлы в список
                for file in file_group:
                    languages_listbox.insert(END, file)
                languages_listbox.insert(END, "\n")


def filter_with_size_scan():
    """Группирует файлы по размеру и удаляет уникальные"""
    size_dict = defaultdict(list)

    for root_dir, _, files in os.walk(file_path):  # Рекурсивный обход папок
        for file in files:
            file_full_path = os.path.join(root_dir, file)  # Изменено имя переменной
            try:
                file_size = os.path.getsize(file_full_path)  # Получаем размер файла
                size_dict[file_size].append(file_full_path)  # Группируем файлы по размеру
            except (PermissionError, FileNotFoundError):
                continue  # Игнорируем файлы, к которым нет доступа

    # Убираем файлы с уникальным размером
    return {size: paths for size, paths in size_dict.items() if len(paths) > 1}


def fast_byte_scan(size_groups, num_bytes=1024):
    """Группирует файлы по первым `num_bytes` байтам"""

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
                continue  # Пропускаем недоступные файлы

            temp_dict[first_bytes].append(file)  # Группируем по первым байтам

        # Оставляем только те группы, где более одного файла
        byte_groups[size] = {k: v for k, v in temp_dict.items() if len(v) > 1}

    return byte_groups


root = create_window()



delete_button = ttk.Button(root, text="Удалить выбранные", command=delete_selected_files)
delete_button.pack(pady=5)

root.mainloop()
