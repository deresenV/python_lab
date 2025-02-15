from tkinter import *
from tkinter import ttk


def create_window(x,y):
    root = Tk()
    root.geometry(f'{x}x{y}')
    root.title("Light'em up!")
    icon = PhotoImage(file="sprite/view_app/logo.png")
    root.iconphoto(False, icon)
    return root

def settings_btn(): # Функция окна настроек
    settings_window = Toplevel(root)
    settings_window.title("Настройки")
    settings_window.geometry("300x200")
    ttk.Button(settings_window, text="Закрыть", command=settings_window.destroy).place(x=205,y=170, width=95, height=30)
root=create_window(480, 480)

ttk.Button(root, text="Settings", command=settings_btn).place(x=0, y=0) # Настройки


root.mainloop()