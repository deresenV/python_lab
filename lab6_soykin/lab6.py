import tkinter
import hashlib
import os
import threading
from tkinter import filedialog, ttk


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
    file_path = filedialog.askdirectory(title="Select Profile Picture")
    ttk.Label(root, text=f"Выбрана директория:{file_path}").pack(anchor=tkinter.CENTER)
    ttk.Button(root, text="Начать поиск", command=start_scan).pack(anchor=tkinter.CENTER)

def start_scan():
    pass


def filter_with_size_scan():
    pass

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
