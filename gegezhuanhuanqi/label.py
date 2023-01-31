import os
from tkinter import Label, PhotoImage


class Labell:
    def __init__(self, parent):
        self.parent = parent
        self.imgs = {}
        self.imgs_path = None
        self.imgs_length = 0
        self.imgs_index = 0
        self.create()

    def get_imgs_path(self):
        if not self.imgs_path:
            self.imgs_path = [
                p for p in os.listdir(os.environ.get('PICTURE_PATH')) if p.endswith('.png')
            ]
            self.imgs_length = len(self.imgs_path)
        self.imgs_index += 1
        if self.imgs_index >= self.imgs_length:  # img maxcount
            self.imgs_index = 0
        file = self.imgs_path[self.imgs_index]
        path = os.path.join(os.environ.get('PICTURE_PATH'), file)
        return path

    def get_img(self):
        path = self.get_imgs_path()
        img = self.imgs.get(path, None)
        if img:
            return img
        img = PhotoImage(file=path)
        self.imgs[path] = img
        return img

    def create(self):
        img = self.get_img()
        self.label = Label(
            self.parent,
            image=img,
            bd=0.5,

        )
        self.label.image = img
        self.label.bind('<ButtonPress-1>', self.change_img)
        self.label.pack()

    def change_img(self, event):
        img = self.get_img()
        self.label.configure(image=img)  # update current image
        self.label.image = img
