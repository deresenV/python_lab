import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

class BlockButton(Button):
    def __init__(self, parent,x,y, img_path, index, buttons_list, field_size):
        super().__init__(parent, command=self.rotate_image)
        self.field_size = field_size
        self.index = index  # Запоминаем индекс кнопки
        self.buttons_list = buttons_list
        # Загружаем изображение
        self.original_image = Image.open(img_path).resize((self.field_size, self.field_size))
        self.current_image = self.original_image.copy()  # Создаём копию
        # Конвертируем в PhotoImage
        self.tk_image = ImageTk.PhotoImage(self.current_image)
        # Устанавливаем изображение на кнопку
        self.config(image=self.tk_image)
        self.place(x=x, y=y)

        # Сохраняем ссылку, чтобы Python не удалил
        self.image = self.tk_image
    def rotate_image(self):
        pass
