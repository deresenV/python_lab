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
        super().__init__(parent, command=self.rotate_image)
        self.img_path = img_path
        self.field_size = field_size
        self.x=x
        self.y=y
        self.index = index  # Запоминаем индекс кнопки
        self.buttons_list = buttons_list
        self.size_field = 480//self.field_size
        self.add_img()
        self.color=color


    def set_on(self):
        self.color='yellow'
        self.img_path=self.img_path.replace('off', 'on')
        self.add_img()


    def check_neighbors(self, main_img, main_index): #Проверка соседей при нажатии на блок
        # self это next elemnt
        # main - нажатый
        print(self.img_path, self.index)
        print(main_img, main_index)
        print("\n")
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



    def check_btn_list(self):
        # print(self.img_path)
        for btn in self.buttons_list:
            # print(f"self:{self.index} btn:{btn.index} size:{self.size_field} del:{(abs(self.index-btn.index)/10)} min:{abs(self.index-btn.index)}")
            if ((abs(self.index - btn.index) == 1 or (abs(self.index - btn.index) / self.size_field) == 1) and btn.index!=self.index and abs(self.index%10-btn.index%10)!=9):
                if btn.check_neighbors(self.img_path, self.index):
                    print('yes')
                    self.set_on()
                    btn.check_btn_list()
                else:
                    print("no")


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
        elif self.img_path in (blocks_paths_on[0], blocks_paths_on[0]) and self.index != 0:
            self.img_path = blocks_paths_off[1]
        elif self.img_path in (blocks_paths_on[1], blocks_paths_on[1]) and self.index != 0:
            self.img_path = blocks_paths_off[3]
        elif self.img_path in (blocks_paths_on[2], blocks_paths_on[2]) and self.index != 0:
            self.img_path = blocks_paths_off[0]
        elif self.img_path in (blocks_paths_on[3], blocks_paths_on[3]) and self.index != 0:
            self.img_path = blocks_paths_off[2]

        if self.index == 0:
            if self.img_path == blocks_paths_on[4]:
                self.img_path = 'sprite/game_block/vertical_on.png'
            elif self.img_path == blocks_paths_on[5]:
                self.img_path = 'sprite/game_block/horizontal_on.png'

        self.add_img()
        self.color="dark"
        self.check_btn_list()

