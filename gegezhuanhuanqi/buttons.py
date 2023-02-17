from tkinter import GROOVE, Button

from gegezhuanhuanqi.core import register


class Buttonn:
    def __init__(self, root, box):
        self.root = root
        self.box = box
        self.choice = 0
        self.create()

    def create(self):
        self.add_delete()
        self.add_clear()
        self.btn1 = self.add_pdfs_to_pdf()
        self.btn2 = self.add_imgs_to_pdf()
        self.btn3 = self.add_word_to_pdf()

    def add_clear(self):
        self.b_clear = Button(
            self.root,
            text="全部清空",
            command=self.box.clear,
            relief=GROOVE,
            width=20,
            height=2
        )
        self.b_clear.grid(row=0, column=1)

    def add_delete(self):
        self.b_delete = Button(
            self.root,
            text="移除单条",
            command=self.box.delete,
            relief=GROOVE,
            width=20,
            height=2
        )
        self.b_delete.grid(row=0, column=0)

    def add_pdfs_to_pdf(self):
        btn = Button(
            self.root,
            text="合并PDF",
            command=register.tags['pdf_imgs'](choice='pdfs', box=self.box),
            relief=GROOVE,
            width=20,
            height=2
        )
        btn.grid(row=1, column=0)
        return btn

    def add_imgs_to_pdf(self):
        btn = Button(
            self.root,
            text="图片合并成PDF",
            command=register.tags['pdf_imgs'](choice='imgs', box=self.box),
            relief=GROOVE,
            width=20,
            height=2
        )
        btn.grid(row=1, column=1)
        return btn

    def add_word_to_pdf(self):
        btn = Button(
            self.root,
            text="WORD/PDF相互转换",
            command=register.tags['pdf_word'](box=self.box),
            relief=GROOVE,
            width=42,
            height=2
        )
        btn.grid(row=2, column=0, columnspan=2)
        return btn

    def change_functions(self):
        if self.choice == 0:
            self.btn1.configure(
                text='生成.ico文件',
                command=register.tags['img_to_ico'](choice='ico', box=self.box)
            )
            self.choice += 1
        elif self.choice == 1:
            self.btn1.configure(
                text='合并PDF',
                command=register.tags['pdf_imgs'](choice='pdfs', box=self.box)
            )
            self.choice = 0
