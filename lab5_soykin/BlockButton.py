import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

class BlockButton(Button):
    def add_img(self):
        # Загружаем изображение
        self.original_image = Image.open(self.img_path).resize((self.field_size, self.field_size))
        self.current_image = self.original_image.copy()  # Создаём копию
        # Конвертируем в PhotoImage
        self.tk_image = ImageTk.PhotoImage(self.current_image)
        # Устанавливаем изображение на кнопку
        self.config(image=self.tk_image)
        self.place(x=self.x, y=self.y)
        # Сохраняем ссылку, чтобы Python не удалил
        self.image = self.tk_image

    def __init__(self, parent,x,y, img_path, index, buttons_list, field_size):
        super().__init__(parent, command=self.rotate_image)
        self.img_path = img_path
        self.field_size = field_size
        self.x=x
        self.y=y
        self.index = index  # Запоминаем индекс кнопки
        self.buttons_list = buttons_list
        self.add_img()

    def rotate_image(self):
        blocks_paths_off = [
            'sprite/game_block/hip_off_LT_DW.png',
            'sprite/game_block/hip_off_LT_UP.png',
            'sprite/game_block/hip_off_RT_DW.png',
            'sprite/game_block/hip_off_RT_UP.png',
            'sprite/game_block/horizontal_off.png',
            'sprite/game_block/vertical_off.png',
        ]
        if self.img_path == blocks_paths_off[4]:
            self.img_path = 'sprite/game_block/vertical_off.png'
        elif self.img_path == blocks_paths_off[5]:
            self.img_path = 'sprite/game_block/horizontal_off.png'
        elif self.img_path == blocks_paths_off[0]:
            self.img_path = 'sprite/game_block/hip_off_LT_UP.png'
        elif self.img_path == blocks_paths_off[1]:
            self.img_path = 'sprite/game_block/hip_off_RT_UP.png'
        elif self.img_path == blocks_paths_off[2]:
            self.img_path = 'sprite/game_block/hip_off_LT_DW.png'
        elif self.img_path == blocks_paths_off[3]:
            self.img_path = 'sprite/game_block/hip_off_RT_DW.png'
        self.add_img()
