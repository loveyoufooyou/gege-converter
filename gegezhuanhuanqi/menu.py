from tkinter import Menu
from gegezhuanhuanqi.utils import tip_voice


class Menuu:
    def __init__(self, root, buttons):
        self.voice = True
        self.root = root
        self.top_menu = self.add_top()
        self.inner_menu = self.add_inner()
        self.top_menu.add_cascade(label='设置', menu=self.inner_menu)
        self.inner_menu.add_command(label='提示声音开/关', command=self.change_voice)
        self.inner_menu.add_command(label='小黑子食不食油饼', command=tip_voice)
        self.inner_menu.add_command(label='切换功能', command=buttons.change_functions)

    def add_top(self):
        return Menu(self.root)
    
    def add_inner(self):
        return Menu(self.top_menu)

    def show(self, event):
        self.inner_menu.post(event.x_root, event.y_root)

    def change_voice(self):
        self.root.change_voice()
