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

    def get_size():  # Изменение размера игровых блоков
        global field_size
        size = count_block.get()

        if not size.isdigit():  # Проверка на ввод только чисел
            size = 10
        else:
            size = int(size)
            size = max(10, min(100, size))  # Ограничиваем значение от 10 до 100

        field_size = 480//int(size ** 0.5)


    #Работа с размером поля
    ttk.Label(settings_window, text="Кол-во блоков:").place(x=0, y=0, height=30)
    count_block = ttk.Entry(settings_window)
    count_block.place(x=100, y=0, width=50, height=30)
    ttk.Button(settings_window, text="Сохранить", command=get_size).place(x=150, y=0)

    #exit
    ttk.Button(settings_window, text="Закрыть", command=settings_window.destroy).place(x=205,y=170, width=95, height=30)

def new_game():
    pass


root=create_window(480, 480)


frame = ttk.Frame(root)
frame.pack(pady=0)
# Создаём кнопки в строку
ttk.Button(frame, text="Settings", command=settings_btn).grid(row=0, column=0, padx=10)
ttk.Button(frame, text="Quit", command=root.destroy).grid(row=0, column=1, padx=10)
ttk.Button(frame, text="New Game", command=new_game).grid(row=0, column=2, padx=10)
ttk.Button(frame, text="Start", command=new_game).grid(row=0, column=3, padx=10)



root.mainloop()