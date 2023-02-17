import os
import time

from PIL.Image import open as image_open
from pdf2docx import Converter
from PyPDF2 import PdfWriter, PdfReader
from win32com.client import constants
from gegezhuanhuanqi.constants import IMGS
from gegezhuanhuanqi.utils import open_word, tip, make_storage, random_str, Library


register = Library()


def get_storage_path(box):
    paths = box.files
    if not paths:
        return
    storage_path = make_storage(paths[0])
    return paths, storage_path

##################
#   pdfs => pdf  #
#   imgs => pdf  #
##################


@register.tag('pdf_imgs')
def pdfs_or_imgs_to_pdf(choice, box):
    def wrapper():
        paths, storage_path = get_storage_path(box)
        if choice == 'pdfs':
            new_path = combine_with_pdfs(paths, storage_path)
        elif choice == 'imgs':
            new_path = combine_with_pictures(paths, storage_path)
        if new_path:
            box.clear()
            tip(new_path, box.root.voice)
    return wrapper


def combine_with_pdfs(paths, storage_path):
    if not paths:
        return
    pdf_writer = None
    for path in paths:
        if path.endswith('.pdf'):
            if not pdf_writer:
                pdf_writer = PdfWriter()
            pdf_reader = PdfReader(path)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])
    if not pdf_writer:
        return
    filename = random_str()
    new_path = os.path.join(storage_path, f'combined_{filename}.pdf')
    with open(new_path, 'ab') as f:
        pdf_writer.write(f)
    return new_path


def combine_with_pictures(paths, storage_path):
    """
    EnsureDispatch must be used to create here, if you want to run .exe.
    """
    word = None
    for path in paths:
        if path.endswith(IMGS):
            if not word:
                word = open_word()
                word.Visible = False
                doc = word.Documents.Add()
                cursor = word.Selection
            cursor.InlineShapes.AddPicture(path)
            cursor.EndKey(Unit=constants.wdStory)  # move cursor to the end
    if not word:
        return
    filename = random_str()
    new_path = os.path.join(storage_path, 'picture_'+filename+'.pdf')
    doc.SaveAs(FileName=new_path, FileFormat=17)
    time.sleep(0.1)
    doc.Close(SaveChanges=0)
    word.Quit()
    return new_path


###################
#   word => pdf   #
#   pdf  => word  #
###################

@register.tag('pdf_word')
def mutual_conversion_word_pdf(box):
    def wrapper():
        paths, storage_path = get_storage_path(box)
        word = None
        flag = False
        for path in paths:
            if path.endswith('.pdf'):
                flag = pdf_to_word(path, storage_path)
            if path.endswith(('.docx', '.doc')):
                if not word:
                    word = open_word()
                flag = word_to_pdf(path, storage_path, word)
        if word:
            word.Quit()
        if flag:
            box.clear()
            tip(storage_path, box.root.voice)
    return wrapper


def word_to_pdf(path, storage_path, word):
    doc = word.Documents.Open(path, ReadOnly=1)
    _, old_filename = os.path.split(path)
    new_filename, _ = os.path.splitext(old_filename)
    new_path = os.path.join(storage_path, new_filename+'.pdf')
    time.sleep(0.1)
    doc.SaveAs(FileName=new_path, FileFormat=17)
    doc.Close(SaveChanges=0)
    return True


def pdf_to_word(path, storage_path):
    p2w = Converter(path)
    _, old_filename = os.path.split(path)
    new_filename, _ = os.path.splitext(old_filename)
    new_path = os.path.join(storage_path, new_filename+'.docx')
    p2w.convert(new_path, start=0, end=None)
    p2w.close()
    return True


############
#  other   #
############

@register.tag('img_to_ico')
def register_img_to_ico(choice, box):
    def wrapper():
        paths, storage_path = get_storage_path(box)
        flag = False
        if choice == 'ico':
            flag = img_to_ico(paths, storage_path)
        if flag:
            box.clear()
            tip(storage_path, box.root.voice)
    return wrapper


def img_to_ico(paths, storage_path):
    """
    img -> ico
    """
    flag = False
    for path in paths:
        if path.endswith(IMGS):
            flag = True
            img = image_open(path)
            _, old_filename = os.path.split(path)
            new_filename, _ = os.path.splitext(old_filename)
            new_path = os.path.join(storage_path, new_filename+'.ico')
            img.save(new_path)
    return flag
