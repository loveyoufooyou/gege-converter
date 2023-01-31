import windnd
from tkinter import Listbox, END, LEFT


class ListBox:
    def __init__(self, root):
        self.box = None
        self.root = root
        self.index = -1
        self.add()

    @property
    def size(self):
        return self.box.size()

    @property
    def files(self):
        files_tuple = self.box.get(first=0, last=self.size)
        return files_tuple

    def add(self):
        self.box = Listbox(
            self.root,
            width=60,  # characters per line
            height=30,
            bd=1,
            font=('微软雅黑', 10),
            relief='flat',
            activestyle='none',
            cursor='target',  # hang mouse type
            background='#E7E7E7',
            highlightbackground='#E7E7E7',  # (blur) listbox frame color
            highlightcolor='#E7E7E7',  # (focus) listbox frame color
            selectbackground='#BDA9CD',  # select item bg color
            selectforeground='black',  # select item font color
        )
        self.box.bind("<Button-1>", self.get_index)  # left-click
        self.box.bind("<ButtonRelease-1>", self.drag_change_index)
        windnd.hook_dropfiles(self.box, func=self.dragged_files)
        self.box.pack(padx=5, pady=20, side=LEFT)

    def clear(self):
        self.box.delete(0, END)

    def delete(self):
        cur = self.box.curselection()
        if cur and cur[0] >= 0:
            self.box.delete(cur)

    def dragged_files(self, files):
        """
        drag files from dirs to the listbox.
        """
        for file_path in files:
            file_path = file_path.decode('gbk')
            self.box.insert(END, file_path)

    def drag_change_index(self, event):
        """
        drag item to other position.
        """
        newindex = self.box.nearest(event.y)
        if newindex == self.index:
            return
        elif newindex > self.index:
            item = self.box.get(self.index)
            self.box.insert(newindex, item)
            self.box.delete(self.index)
        elif newindex < self.index:
            item = self.box.get(self.index)
            self.box.insert(newindex, item)
            self.box.delete(self.index+1)

    def get_index(self, event):
        """
        click get current index.
        """
        self.index = self.box.nearest(event.y)
