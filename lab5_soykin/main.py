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


    def get_size(): # Изменение размера поля под конкретное кол-во игровых блоков
        size=count_block.get()
        if size=="":
            size=10
        elif int(size)<=10:
            size=10
        root.geometry(f"{int(size)*48}x{int(size)*48}")


    #Работа с размером поля
    ttk.Label(settings_window, text="Кол-во блоков:").place(x=0, y=0, height=30)
    count_block = ttk.Entry(settings_window)
    count_block.place(x=100, y=0, width=50, height=30)
    ttk.Button(settings_window, text="Сохранить", command=get_size).place(x=150, y=0)

    #exit
    ttk.Button(settings_window, text="Закрыть", command=settings_window.destroy).place(x=205,y=170, width=95, height=30)


root=create_window(480, 480)

ttk.Button(root, text="Settings", command=settings_btn).place(x=0, y=0) # Настройки


root.mainloop()