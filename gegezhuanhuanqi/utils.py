import threading
import traceback
import os
import winsound
from datetime import date
from itertools import chain
from tkinter.messagebox import showinfo
from random import choice
from win32com.client.gencache import EnsureDispatch

video_path = os.path.join(os.environ.get('VIDEO_PATH'), 'ngm.wav')


def random_str(length=12):
    """
    65-90: A-Z
    97-122: a-z
    48-58: 0-9
    """
    s = ''
    random_ints = list(chain(range(48, 58), range(65, 91), range(97, 123)))
    for _ in range(length):
        char = choice(random_ints)
        s += chr(char)
    return s


def make_storage(basepath):
    basepath = os.path.dirname(basepath)
    storage_path = os.path.join(basepath, f'storage {date.today()}')
    if not os.path.exists(storage_path):
        os.mkdir(storage_path)
    return storage_path


def open_word():
    try:
        word = EnsureDispatch('Word.Application')
        word.Visible = False
    except Exception as e:
        traceback.print_exc()
    else:
        return word


def run(path):
    winsound.PlaySound(path, winsound.SND_ASYNC and winsound.SND_ALIAS)


def tip_voice():
    t = threading.Thread(target=run, args=(video_path, ))
    t.start()


def tip_message(path):
    showinfo(title='successful', message=f'已成功合并到"{path}"')


def tip(path, voice=True):
    if voice:
        tip_voice()
    tip_message(path)
