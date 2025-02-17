import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

blocks_paths_off = [
    'sprite/game_block/hip_off_LT_DW.png', # 0
    'sprite/game_block/hip_off_LT_UP.png',# 1
    'sprite/game_block/hip_off_RT_DW.png',# 2
    'sprite/game_block/hip_off_RT_UP.png',# 3
    'sprite/game_block/horizontal_off.png',# 4
    'sprite/game_block/vertical_off.png',# 5
]
blocks_paths_on = [
    'sprite/game_block/hip_on_LT_DW.png', # 0
    'sprite/game_block/hip_on_LT_UP.png', # 1
    'sprite/game_block/hip_on_RT_DW.png', # 2
    'sprite/game_block/hip_on_RT_UP.png', # 3
    'sprite/game_block/horizontal_on.png', # 4
    'sprite/game_block/vertical_on.png', # 5
]


class BlockButton(Button):
    def set_on(self):
        self.img_path=self.img_path.replace('off', 'on')
        self.add_img()


    def check_neighbors(self, main_img, main_index): #Проверка соседей при нажатии на блок
        if ((main_img == blocks_paths_on[4] and self.img_path==blocks_paths_off[4] and abs(self.index-main_index)==1) or
                (main_img == blocks_paths_off[4] and self.img_path==blocks_paths_on[4] and abs(self.index-main_index)==1)):
            return True
        if ((main_img == blocks_paths_on[5] and self.img_path==blocks_paths_off[5] and abs(self.index-main_index)==1) or
                (main_img == blocks_paths_off[5] and self.img_path==blocks_paths_on[5] and abs(self.index-main_index)//(480//self.field_size)==1)):
            return True
        if ((main_img == blocks_paths_on[4] and self.img_path==blocks_paths_off[0] and abs(self.index-main_index)==1) or
                (main_img == blocks_paths_off[0] and self.img_path==blocks_paths_on[4] and abs(self.index-main_index)==1)):
            return True



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
        block_mappings = {
            blocks_paths_off[0]: 'sprite/game_block/hip_off_LT_UP.png',
            blocks_paths_off[1]: 'sprite/game_block/hip_off_RT_UP.png',
            blocks_paths_off[2]: 'sprite/game_block/hip_off_LT_DW.png',
            blocks_paths_off[3]: 'sprite/game_block/hip_off_RT_DW.png',
        }

        if self.img_path in block_mappings:
            self.img_path = block_mappings[self.img_path]
        elif self.img_path in (blocks_paths_off[4], blocks_paths_on[4]) and self.index != 0:
            self.img_path = 'sprite/game_block/vertical_off.png'
        elif self.img_path in (blocks_paths_off[5], blocks_paths_on[5]) and self.index != 0:
            self.img_path = 'sprite/game_block/horizontal_off.png'

        if self.index == 0:
            if self.img_path == blocks_paths_on[4]:
                self.img_path = 'sprite/game_block/vertical_on.png'
            elif self.img_path == blocks_paths_on[5]:
                self.img_path = 'sprite/game_block/horizontal_on.png'

        self.add_img()
        for btn in self.buttons_list:
            if btn != self:  # Не сравниваем с самой собой
                if (abs(btn.x - self.x) == self.field_size and btn.y == self.y) or (abs(btn.y - self.y) == self.field_size and btn.x == self.x):
                    if btn.check_neighbors(self.img_path, self.index):
                        self.set_on()

