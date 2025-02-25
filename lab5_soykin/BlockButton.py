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
    def __init__(self, parent,x,y, img_path, index, buttons_list, field_size, color):
        super().__init__(parent, command=self.rotate_image) # Обращение к классу Button из tkinter
        self.img_path = img_path
        self.field_size = field_size
        self.x=x
        self.y=y
        self.index = index  # Запоминаем индекс кнопки
        self.buttons_list = buttons_list
        self.size_field = 480//self.field_size # Размер поля N*N - Переменная N
        self.add_img()
        self.color=color
        if self.index==self.size_field**2-1:
            self.buttons_list[0].check_btn_list()

    def set_on(self):
        """
        Включает блок кнопку
        :return: -
        """
        self.color='yellow'
        self.img_path=self.img_path.replace('off', 'on')
        self.add_img()


    def check_neighbors(self, main_img, main_index):#Проверка соседей при нажатии на блок
        """
        :param main_img: self картинка(нажатая) переданная сюда вместе с кнопкой соседом(self)
        :param main_index: индекс кнопки(нажатой) переданной сюда вместе с кнопкой соседом
        :return: True если соеденены
        """
        # self это next elemnt
        # main - нажатый
        # horizontal+horizontal
        if ((main_img == blocks_paths_on[4] and self.img_path==blocks_paths_off[4] and abs(self.index-main_index)==1) or
                (main_img == blocks_paths_off[4] and self.img_path==blocks_paths_on[4] and abs(self.index-main_index)==1)):
            return True
        # vertical + vertical
        if ((main_img == blocks_paths_on[5] and self.img_path==blocks_paths_off[5] and abs(self.index-main_index)//(480//self.field_size)==1) or
                (main_img == blocks_paths_off[5] and self.img_path==blocks_paths_on[5] and abs(self.index-main_index)//(480//self.field_size)==1)):
            return True
        #horizontal+hip
        if ((main_img == blocks_paths_off[0] and self.img_path==blocks_paths_on[4] and main_index-self.index==1) or
                (main_img == blocks_paths_off[4] and self.img_path == blocks_paths_on[0] and main_index - self.index == -1) or

                (main_img == blocks_paths_off[1] and self.img_path == blocks_paths_on[4] and main_index - self.index == 1) or
                (main_img == blocks_paths_off[4] and self.img_path == blocks_paths_on[1] and main_index - self.index == -1) or

                (main_img == blocks_paths_off[2] and self.img_path == blocks_paths_on[4] and main_index - self.index == -1) or
                (main_img == blocks_paths_off[4] and self.img_path == blocks_paths_on[2] and main_index - self.index == 1) or

                (main_img == blocks_paths_off[3] and self.img_path == blocks_paths_on[4] and main_index - self.index == -1) or
                (main_img == blocks_paths_off[4] and self.img_path == blocks_paths_on[3] and main_index - self.index == 1) or


                (main_img == blocks_paths_on[0] and self.img_path == blocks_paths_off[
                    4] and main_index - self.index == 1) or
                (main_img == blocks_paths_on[4] and self.img_path == blocks_paths_off[
                    0] and main_index - self.index == -1) or

                (main_img == blocks_paths_on[1] and self.img_path == blocks_paths_off[
                    4] and main_index - self.index == 1) or
                (main_img == blocks_paths_on[4] and self.img_path == blocks_paths_off[
                    1] and main_index - self.index == -1) or

                (main_img == blocks_paths_on[2] and self.img_path == blocks_paths_off[
                    4] and main_index - self.index == -1) or
                (main_img == blocks_paths_on[4] and self.img_path == blocks_paths_off[
                    2] and main_index - self.index == 1) or

                (main_img == blocks_paths_on[3] and self.img_path == blocks_paths_off[
                    4] and main_index - self.index == -1) or
                (main_img == blocks_paths_on[4] and self.img_path == blocks_paths_off[
                    3] and main_index - self.index == 1)

        ):
            return True
        #vertical+hip
        if ((main_img==blocks_paths_off[1] and self.img_path==blocks_paths_on[5] and main_index-self.index==self.size_field) or
                (main_img == blocks_paths_off[5] and self.img_path == blocks_paths_on[1] and main_index - self.index == -self.size_field) or

                (main_img == blocks_paths_off[3] and self.img_path == blocks_paths_on[5] and main_index - self.index == self.size_field) or
                (main_img == blocks_paths_off[5] and self.img_path == blocks_paths_on[3] and main_index - self.index == -self.size_field) or

                (main_img==blocks_paths_off[5] and self.img_path==blocks_paths_on[0] and main_index-self.index==self.size_field) or
                (main_img == blocks_paths_off[0] and self.img_path == blocks_paths_on[5] and main_index - self.index == -self.size_field) or

                (main_img == blocks_paths_off[5] and self.img_path == blocks_paths_on[2] and main_index - self.index == self.size_field) or
                (main_img == blocks_paths_off[2] and self.img_path == blocks_paths_on[5] and main_index - self.index == -self.size_field) or

                (main_img == blocks_paths_on[1] and self.img_path == blocks_paths_off[
                    5] and main_index - self.index == self.size_field) or
                (main_img == blocks_paths_on[5] and self.img_path == blocks_paths_off[
                    1] and main_index - self.index == -self.size_field) or

                (main_img == blocks_paths_on[3] and self.img_path == blocks_paths_off[
                    5] and main_index - self.index == self.size_field) or
                (main_img == blocks_paths_on[5] and self.img_path == blocks_paths_off[
                    3] and main_index - self.index == -self.size_field) or

                (main_img == blocks_paths_on[5] and self.img_path == blocks_paths_off[
                    0] and main_index - self.index == self.size_field) or
                (main_img == blocks_paths_on[0] and self.img_path == blocks_paths_off[
                    5] and main_index - self.index == -self.size_field) or

                (main_img == blocks_paths_on[5] and self.img_path == blocks_paths_off[
                    2] and main_index - self.index == self.size_field) or
                (main_img == blocks_paths_on[2] and self.img_path == blocks_paths_off[
                    5] and main_index - self.index == -self.size_field)

        ):
            return True

        #hip+hip
        if ((main_img==blocks_paths_off[1] and self.img_path==blocks_paths_on[3] and main_index-1==self.index) or
                (main_img == blocks_paths_off[3] and self.img_path == blocks_paths_on[1] and main_index+1 == self.index)
        ):
            return True
        if ((main_img==blocks_paths_off[0] and self.img_path==blocks_paths_on[2] and main_index-1==self.index) or
                (main_img == blocks_paths_off[2] and self.img_path == blocks_paths_on[0] and main_index + 1 == self.index)

        ):
            return True
        if ((main_img==blocks_paths_off[0] and self.img_path==blocks_paths_on[3] and main_index-1==self.index) or
                (main_img == blocks_paths_off[3] and self.img_path == blocks_paths_on[0] and main_index + 1 == self.index)
        ):
            return True
        if ((main_img==blocks_paths_off[1] and self.img_path==blocks_paths_on[2] and main_index-1==self.index) or
                (main_img == blocks_paths_off[2] and self.img_path == blocks_paths_on[1] and main_index + 1 == self.index)

        ):
            return True
        #hip+hip vertical
        if ((main_img==blocks_paths_off[3] and self.img_path==blocks_paths_on[2] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_off[2] and self.img_path == blocks_paths_on[3] and main_index + self.size_field == self.index)

        ):
            return True
        if ((main_img==blocks_paths_off[3] and self.img_path==blocks_paths_on[0] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_off[0] and self.img_path == blocks_paths_on[3] and main_index + self.size_field == self.index)

        ):
            return True
        if ((main_img==blocks_paths_off[1] and self.img_path==blocks_paths_on[0] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_off[0] and self.img_path == blocks_paths_on[1] and main_index + self.size_field == self.index)
        ):
            return True
        if ((main_img==blocks_paths_off[1] and self.img_path==blocks_paths_on[2] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_off[2] and self.img_path == blocks_paths_on[1] and main_index + self.size_field == self.index)

        ):
            return True

        if ((main_img==blocks_paths_on[1] and self.img_path==blocks_paths_off[3] and main_index-1==self.index) or
                (main_img == blocks_paths_on[3] and self.img_path == blocks_paths_off[1] and main_index+1 == self.index)
        ):
            return True
        if ((main_img==blocks_paths_on[0] and self.img_path==blocks_paths_off[2] and main_index-1==self.index) or
                (main_img == blocks_paths_on[2] and self.img_path == blocks_paths_off[0] and main_index + 1 == self.index)

        ):
            return True
        if ((main_img==blocks_paths_on[0] and self.img_path==blocks_paths_off[3] and main_index-1==self.index) or
                (main_img == blocks_paths_on[3] and self.img_path == blocks_paths_off[0] and main_index + 1 == self.index)
        ):
            return True
        if ((main_img==blocks_paths_on[1] and self.img_path==blocks_paths_off[2] and main_index-1==self.index) or
                (main_img == blocks_paths_on[2] and self.img_path == blocks_paths_off[1] and main_index + 1 == self.index)

        ):
            return True
        #hip+hip vertical
        if ((main_img==blocks_paths_on[3] and self.img_path==blocks_paths_off[2] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_on[2] and self.img_path == blocks_paths_off[3] and main_index + self.size_field == self.index)

        ):
            return True
        if ((main_img==blocks_paths_on[3] and self.img_path==blocks_paths_off[0] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_on[0] and self.img_path == blocks_paths_off[3] and main_index + self.size_field == self.index)

        ):
            return True
        if ((main_img==blocks_paths_on[1] and self.img_path==blocks_paths_off[0] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_on[0] and self.img_path == blocks_paths_off[1] and main_index + self.size_field == self.index)
        ):
            return True
        if ((main_img==blocks_paths_on[1] and self.img_path==blocks_paths_off[2] and main_index-self.size_field==self.index) or
                (main_img == blocks_paths_on[2] and self.img_path == blocks_paths_off[1] and main_index + self.size_field == self.index)

        ):
            return True


    def set_off_all(self):
        """
        Выключает все кнопки
        :return: off img_path
        """
        for btn in self.buttons_list[1:]:
            if btn.color=="yellow":
                btn.img_path=btn.img_path.replace("_on", "_off")
                btn.add_img()
                btn.color="dark"


    def check_btn_list(self):
        """
        Проверяет соседей на подходимость двигаясь в глубину(Рекурсивно условно)
        :return: Загорает клавиши
        """
        for btn in self.buttons_list:
            if ((abs(self.index - btn.index) == 1 or (abs(self.index - btn.index) / self.size_field) == 1) and btn.index!=self.index and abs(self.index%self.size_field-btn.index%self.size_field)!=self.size_field-1):
                if btn.check_neighbors(self.img_path, self.index):
                    self.set_on()
                    btn.check_btn_list()

        for btn in self.buttons_list[::-1]:
            if ((abs(self.index - btn.index) == 1 or (abs(self.index - btn.index) / self.size_field) == 1) and btn.index!=self.index and abs(self.index%self.size_field-btn.index%self.size_field)!=self.size_field-1):
                if btn.check_neighbors(self.img_path, self.index):
                    self.set_on()
                    btn.check_btn_list()


    def add_img(self):
        """
        Натягивает изображение на кнопку
        :return: сохраненная текстура(чтоб не пропала)+текстура на блоке
        """
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

    def rotate_image(self):
        """
        Крутит изображение блока меняя его текстуру
        :return: Повернутая и с нужным цветом кнопка блок
        """
        block_mappings_off = {
            blocks_paths_off[0]: 'sprite/game_block/hip_off_LT_UP.png',
            blocks_paths_off[1]: 'sprite/game_block/hip_off_RT_UP.png',
            blocks_paths_off[2]: 'sprite/game_block/hip_off_LT_DW.png',
            blocks_paths_off[3]: 'sprite/game_block/hip_off_RT_DW.png',
        }

        block_mappings_on = {
            blocks_paths_on[0]: 'sprite/game_block/hip_on_LT_UP.png',
            blocks_paths_on[1]: 'sprite/game_block/hip_on_RT_UP.png',
            blocks_paths_on[2]: 'sprite/game_block/hip_on_LT_DW.png',
            blocks_paths_on[3]: 'sprite/game_block/hip_on_RT_DW.png',
        }

        if self.img_path in block_mappings_off:
            self.img_path = block_mappings_off[self.img_path]
        elif self.img_path in block_mappings_on and self.index==0:
            self.img_path = block_mappings_on[self.img_path]
        elif self.img_path in (blocks_paths_off[4], blocks_paths_on[4]) and self.index != 0:
            self.img_path = 'sprite/game_block/vertical_off.png'
        elif self.img_path in (blocks_paths_off[5], blocks_paths_on[5]) and self.index != 0:
            self.img_path = 'sprite/game_block/horizontal_off.png'
        elif self.img_path == blocks_paths_on[0] and self.index != 0:
            self.img_path = blocks_paths_off[1]
        elif self.img_path == blocks_paths_on[1] and self.index != 0:
            self.img_path = blocks_paths_off[3]
        elif self.img_path == blocks_paths_on[2] and self.index != 0:
            self.img_path = blocks_paths_off[0]
        elif self.img_path == blocks_paths_on[3] and self.index != 0:
            self.img_path = blocks_paths_off[2]

        if self.index == 0:
            block_mappings_special = {
                blocks_paths_on[4]: 'sprite/game_block/vertical_on.png',
                blocks_paths_on[5]: 'sprite/game_block/horizontal_on.png'
            }
            self.img_path = block_mappings_special.get(self.img_path, self.img_path)

        self.add_img()

        self.color = "dark" # Меняет кнпоку на негорящую если повернули(В set_on меняем заново на нужный если она горит)

        #Проверка в глубину всех кнопок
        self.check_btn_list()
        self.set_off_all()
        self.buttons_list[0].check_btn_list()

