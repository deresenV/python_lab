import json
import random
from tkinter import *
from tkinter import ttk

from lab5_soykin.BlockButton import BlockButton

total_time = 120 # Время в секундах
field_size = 48  # Размер игрового блока
progress = None  # Полоска прогресса
stop_btn = None  # Кнопка "Stop"
time_left = total_time  # Время, оставшееся на таймере
timer_id = None  # ID таймера для `after`
game_blocks=None
game_blocksw=None
count=0
blocks_paths_off = [
    ['sprite/game_block/hip_off_LT_DW.png',
    'sprite/game_block/hip_off_LT_UP.png',
    'sprite/game_block/hip_off_RT_DW.png',
    'sprite/game_block/hip_off_RT_UP.png',
     ],
    ['sprite/game_block/horizontal_off.png'],
    ['sprite/game_block/vertical_off.png'],
]
blocks_paths_on = [
    'sprite/game_block/hip_on_LT_DW.png', # 0
    'sprite/game_block/hip_on_LT_UP.png', # 1
    'sprite/game_block/hip_on_RT_DW.png', # 2
    'sprite/game_block/hip_on_RT_UP.png', # 3
    'sprite/game_block/horizontal_on.png', # 4
    'sprite/game_block/vertical_on.png', # 5
]

def create_window(width, height):
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")
    root.title("Light'em up!")
    icon = PhotoImage(file="sprite/view_app/logo.png")
    root.iconphoto(False, icon)
    return root


def toggle():
    print(f"Состояние: {var.get()}")  # 1 — включено, 0 — выключено


def settings_btn():  # Функция окна настроек
    settings_window = Toplevel(root)
    settings_window.title("Настройки")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - 300) // 2
    y = (screen_height - 200) // 2

    settings_window.geometry(f"{300}x{200}+{x}+{y}")

    def get_size():  # Изменение размера игровых блоков
        global field_size, var
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
    ttk.Label(settings_window, text="Прегенерация:").place(x=0, y=60, height=30)
    ttk.Checkbutton(settings_window, variable=var, command=toggle).place(x=100, y=60, height=30)
    # Выход
    ttk.Button(settings_window, text="Закрыть", command=settings_window.destroy).place(x=205, y=170, width=95, height=30)

def return_button(): # возврат кнопок
    start_game.grid(row=0, column=3, padx=10)
    settings_button.grid(row=0, column=0, padx=10)


def stop_button():
    global progress, stop_btn, timer_id, time_left, game_blocks, game_blocksw
    if timer_id:
        root.after_cancel(timer_id)  # Останавливаем таймер
        timer_id = None
    if progress:
        progress.destroy()  # Удаляем полоску прогресса
        progress = None
    if stop_btn:
        stop_btn.destroy()  # Удаляем кнопку "Stop"
        stop_btn = None
    # Удаление всех кнопок из game_blocks
    if game_blocks:
        for btn in game_blocks:
            btn.destroy()
        game_blocks.clear()  # Очищаем список
    if game_blocksw:
        for btn in game_blocksw:
            btn.destroy()
        game_blocksw.clear()  # Очищаем список

    time_left = total_time  # Сбрасываем таймер
    return_button()

def replace_img_json(value):
    if "hip" in value:
        return "hip"
    if "line" in value:
        return "line"
    return "all"

def replace_img_paths(values):
    img_paths = values.replace("hip", f"{random.choice(blocks_paths_off[0])}").replace("line", f"{random.choice([blocks_paths_off[1][0], blocks_paths_off[2][0]])}").replace("all", f"{random.choice(blocks_paths_off)[0]}")
    return img_paths

def create_game_block(): # Создание игрового поля
    global game_blocks
    game_blocks=[]
    i=0 # index
    #Координаты 28> - верхние кнопки
    y_blocks=28
    x_blocks=0
    if var.get()==0:
        for y in range(480//field_size):
            x_blocks=0
            for x in range(480//field_size):
                img_paths=random.choice(random.choice(blocks_paths_off))
                if i==0:
                    btn=BlockButton(root,x_blocks,y_blocks,'sprite/game_block/hip_on_LT_UP.png',i,game_blocks, field_size,'yellow')
                else:
                    btn=BlockButton(root,x_blocks,y_blocks,img_paths,i, game_blocks, field_size,'dark')
                game_blocks.append(btn)
                i+=1
                x_blocks+=field_size

            y_blocks+=field_size
    else:
        with open(f"maps/map_{480//field_size}x{480//field_size}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        # Извлекаем все значения из вложенных списков
        values = [replace_img_json(value) for rows in data[f"{random.randint(1, len(data))}"].values() for value in rows]
        for y in range(480//field_size):
            x_blocks=0
            for x in range(480//field_size):
                img_paths=replace_img_paths(values[i])
                if i==0:
                    btn = BlockButton(root, x_blocks, y_blocks, 'sprite/game_block/hip_on_LT_UP.png', i, game_blocks, field_size, 'yellow')
                else:
                    btn = BlockButton(root, x_blocks, y_blocks, img_paths, i, game_blocks, field_size, 'dark')
                game_blocks.append(btn)
                i += 1
                x_blocks += field_size
            y_blocks += field_size

def create_game_answer():
    global game_blocksw
    if var.get()==0:
        return 0
    else:
        y_blocks=28
        game_blocksw=[]
        i=0
        with open(f"maps/map_{480 // field_size}x{480 // field_size}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        # Извлекаем все значения из вложенных списков
        values = [value for rows in data[f"{random.randint(1, len(data))}"].values() for value in rows]
        for y in range(480 // field_size):
            x_blocks = 0
            for x in range(480 // field_size):
                img_paths=((values[i].replace("hip_rd",f'{blocks_paths_on[2]}').replace("hip_ld",f"{blocks_paths_on[0]}")
                           .replace("hip_ru",f'{blocks_paths_on[3]}').replace("hip_lu",f"{blocks_paths_on[1]}"))
                           .replace("line_v",f"{blocks_paths_on[5]}")).replace("line_h",f"{blocks_paths_on[4]}")
                btn = BlockButton(root, x_blocks, y_blocks, img_paths, i, game_blocksw, field_size, 'yellow')
                game_blocksw.append(btn)
                i += 1
                x_blocks += field_size
            y_blocks += field_size


def result_game(text):  # Если закончилось время
    stop_button()  # Удаляем таймер и кнопку
    lose_window = Toplevel(root)
    lose_window.title("Результаты")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - 300) // 2
    y = (screen_height - 200) // 2

    lose_window.geometry(f"{300}x{200}+{x}+{y}")
    ttk.Label(lose_window, text=text,font=("Arial", 36)).pack(anchor=CENTER)
    ttk.Button(lose_window, text="Выйти из игры", command=root.destroy).pack(anchor=CENTER)
    ttk.Button(lose_window, text="Играть", command=lambda: (new_game(), lose_window.destroy())).pack(anchor=CENTER)
    create_game_answer()


def new_game():  # Старт игры с таймером
    global progress, stop_btn, time_left, timer_id
    count=0
    stop_button()  # Очищаем предыдущее состояние игры (удаляет кнопки)

    create_game_block()  # Теперь создаём новые кнопки

    # Скрываем кнопку старта и настроек
    start_game.grid_forget()
    settings_button.grid_forget()

    # Создаём новую полоску прогресса
    progress = ttk.Progressbar(root, length=480, mode="determinate")
    progress.place(x=0, y=y_size - 30, height=30)

    # Создаём кнопку "Stop"
    stop_btn = ttk.Button(frame, text="Stop", command=stop_button)
    stop_btn.grid(row=0, column=1, padx=10)

    # Функция обновления таймера
    def update_timer():
        global time_left, timer_id, count
        if time_left > 0:
            if True:
                count=0
                for btn in game_blocks:
                    if btn.img_path.count("_on") == 1:
                        count+=1
                    if count==(480//field_size)**2:
                        stop_button()
                        result_game("Вы выиграли!")
            time_left -= 1

            if progress:
                progress["value"] = (total_time - time_left) / total_time * 100  # Заполняем полоску
            timer_id = root.after(1000, update_timer)  # Запускаем снова через 1 сек
        else:  # Если время вышло
            result_game("Вы проиграли")

    # Сбрасываем таймер и запускаем его
    time_left = total_time
    progress["value"] = 0
    update_timer()


# Окно игры
y_size = 480 + 28 + 30
root = create_window(480, y_size)
var = IntVar()  # Переменная для хранения состояния
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
