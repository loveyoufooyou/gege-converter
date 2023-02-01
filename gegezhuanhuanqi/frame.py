from tkinter import LEFT, TOP, Frame


class Framee():
    def __init__(self, root):
        self.root = root
        self.frame = None
        

    def add_main(self):
        self.frame = Frame(
            self.root,
            background='#84B2E7'
        )
        self.frame.pack(padx=5, pady=20, side=LEFT)

    def add(self):
        self.frame = Frame(
            self.root,
            bd=0
        )
        self.frame.pack(pady=1, side=TOP)
