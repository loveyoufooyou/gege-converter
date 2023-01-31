from tkinter import GROOVE, Button
from gegezhuanhuanqi.core import mutual_conversion_word_pdf, pdfs_or_imgs_to_pdf


class Buttonn:
    def __init__(self, root):
        self.root = root

    def add_clear(self, box):
        self.b_clear = Button(
            self.root,
            text="全部清空",
            command=box.clear,
            relief=GROOVE,
            width=20,
            height=2
        )
        self.b_clear.grid(row=0, column=1)

    def add_delete(self, box):
        self.b_delete = Button(
            self.root,
            text="移除单条",
            command=box.delete,
            relief=GROOVE,
            width=20,
            height=2
        )
        self.b_delete.grid(row=0, column=0)

    def add_pdfs_to_pdf(self, box):
        self.b_pdfs_to_pdf = Button(
            self.root,
            text="合并PDF",
            command=pdfs_or_imgs_to_pdf(choice='pdfs', box=box),
            relief=GROOVE,
            width=20,
            height=2
        )
        self.b_pdfs_to_pdf.grid(row=1, column=0)

    def add_imgs_to_pdf(self, box):
        self.b_imgs_to_pdf = Button(
            self.root,
            text="图片合并成PDF",
            command=pdfs_or_imgs_to_pdf(choice='imgs', box=box),
            relief=GROOVE,
            width=20,
            height=2
        )
        self.b_imgs_to_pdf.grid(row=1, column=1)

    def add_word_to_pdf(self, box):
        self.b_word_to_pdf = Button(
            self.root,
            text="WORD/PDF相互转换",
            command=mutual_conversion_word_pdf(box=box),
            relief=GROOVE,
            width=42,
            height=2
        )
        self.b_word_to_pdf.grid(row=2, column=0, columnspan=2)
