import os
from tkinter import Tk


class Root(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False, False)
        self.title("鸽鸽转换器")
        self.configure(bg='#84B2E7')
        path = os.path.join(os.environ.get('PICTURE_PATH'), 'gege.ico')
        self.iconbitmap(path)
        self.voice = True  # gege voice
        width = 800
        height = 500
        scn_width, scn_height = self.maxsize()
        whxy = '%dx%d+%d+%d' % (
            width,
            height,
            (scn_width-scn_height)/2,
            (scn_height-height)/2
        )
        self.geometry(whxy)
        self.update()

    def change_voice(self):
        self.voice = not self.voice
