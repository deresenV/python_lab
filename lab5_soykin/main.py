from tkinter import *
from tkinter import ttk

total_time = 5  # Время в секундах
field_size = 48  # Размер игрового блока
progress = None  # Полоска прогресса
stop_btn = None  # Кнопка "Stop"

def create_window(x, y):
    root = Tk()
    root.geometry(f'{x}x{y}')
    root.title("Light'em up!")
    icon = PhotoImage(file="sprite/view_app/logo.png")
    root.iconphoto(False, icon)
    return root

def settings_btn():  # Функция окна настроек
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

        field_size = 480 // int(size ** 0.5)

    # Работа с размером поля
    ttk.Label(settings_window, text="Кол-во блоков:").place(x=0, y=0, height=30)
    count_block = ttk.Entry(settings_window)
    count_block.place(x=100, y=0, width=50, height=30)
    ttk.Button(settings_window, text="Сохранить", command=get_size).place(x=150, y=0)

    # Выход
    ttk.Button(settings_window, text="Закрыть", command=settings_window.destroy).place(x=205, y=170, width=95, height=30)

def return_button():
    start_game.grid(row=0, column=3, padx=10)
    settings_button.grid(row=0, column=0, padx=10)

def stop_button():
    global progress, stop_btn
    if progress:
        progress.destroy()  # Удаляем полоску прогресса
        progress = None
    if stop_btn:
        stop_btn.destroy()  # Удаляем кнопку "Stop"
        stop_btn = None
    return_button()

def lose_game():  # Если закончилось время
    stop_button()  # Удаляем таймер и кнопку
    print("Вы проиграли!")  # Для теста

def new_game():  # Старт игры с таймером
    global progress, stop_btn, time_left

    # Скрываем кнопку старта и настроек
    start_game.grid_forget()
    settings_button.grid_forget()

    # Если уже есть progress bar — удаляем его, чтобы не создавать новый
    if progress:
        progress.destroy()
    progress = ttk.Progressbar(root, length=480, mode="determinate")
    progress.place(x=10, y=150, height=30)

    # Если кнопка "Stop" уже существует, удаляем её
    if stop_btn:
        stop_btn.destroy()
    stop_btn = ttk.Button(frame, text="Stop", command=stop_button)
    stop_btn.grid(row=0, column=1, padx=10)

    # Функция обновления таймера
    def update_timer():
        global time_left
        if time_left > 0:
            time_left -= 1
            if progress:
                progress["value"] = (total_time - time_left) / total_time * 100  # Заполняем полоску
                root.after(1000, update_timer)  # Запускаем снова через 1 сек
        else:  # Если время вышло
            lose_game()

    # Сбрасываем таймер и запускаем его
    time_left = total_time
    progress["value"] = 0
    update_timer()

# Окно игры
y_size = 480 + 28 + 30
root = create_window(480, y_size)

frame = ttk.Frame(root)
frame.pack(pady=0)

# Создаём кнопки в строку
settings_button = ttk.Button(frame, text="Settings", command=settings_btn)
settings_button.grid(row=0, column=0, padx=10)
ttk.Button(frame, text="Quit", command=root.destroy).grid(row=0, column=1, padx=10)
ttk.Button(frame, text="New Game", command=new_game).grid(row=0, column=2, padx=10)
start_game = ttk.Button(frame, text="Start", command=new_game)
start_game.grid(row=0, column=3, padx=10)

root.mainloop()
