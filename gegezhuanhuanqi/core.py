import os
import time
from pdf2docx import Converter
from PyPDF2 import PdfWriter, PdfReader
from win32com.client import constants
from gegezhuanhuanqi.utils import open_word, tip, make_storage, random_str
from gegezhuanhuanqi.constants import IMGS


def pdfs_or_imgs_to_pdf(choice, box):
    def func():
        paths = box.files
        if not paths:
            return
        storage_path = make_storage(paths[0])
        if choice == 'pdfs':
            new_path = combine_with_pdfs(paths, storage_path)
        elif choice == 'imgs':
            new_path = combine_with_pictures(paths, storage_path)
        box.clear()
        tip(new_path, box.root.voice)
    return func


def combine_with_pdfs(paths, storage_path):
    pdf_writer = PdfWriter()
    if not paths:
        return
    for path in paths:
        if path.endswith('.pdf'):
            pdf_reader = PdfReader(path)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])
    filename = random_str()
    new_path = os.path.join(storage_path, f'combined_{filename}.pdf')
    with open(new_path, 'ab') as f:
        pdf_writer.write(f)
    return new_path


def combine_with_pictures(paths, storage_path):
    """
    EnsureDispatch must be used to create here, if you want to run .exe.
    """
    word = open_word()
    word.Visible = False
    doc = word.Documents.Add()
    cursor = word.Selection
    for path in paths:
        if path.endswith(IMGS):
            cursor.InlineShapes.AddPicture(path)
            cursor.EndKey(Unit=constants.wdStory)  # move cursor to the end
    filename = random_str()
    new_path = os.path.join(storage_path, 'picture_'+filename+'.pdf')
    doc.SaveAs(FileName=new_path, FileFormat=17)
    time.sleep(0.1)
    doc.Close(SaveChanges=0)
    word.Quit()
    return new_path


def mutual_conversion_word_pdf(box):
    def func():
        paths = box.files
        if not paths:
            return
        storage_path = make_storage(paths[0])
        word = None
        for path in paths:
            if path.endswith('.pdf'):
                pdf_to_word(path, storage_path)
            if path.endswith(('.docx', '.doc')):
                if not word:
                    word = open_word()
                word_to_pdf(path, storage_path, word)
        if word:
            word.Quit()
        box.clear()
        tip(storage_path, box.root.voice)
    return func


def word_to_pdf(path, storage_path, word):
    doc = word.Documents.Open(path, ReadOnly=1)
    _, old_filename = os.path.split(path)
    new_filename, _ = os.path.splitext(old_filename)
    new_path = os.path.join(storage_path, new_filename+'.pdf')
    time.sleep(0.1)
    doc.SaveAs(FileName=new_path, FileFormat=17)
    doc.Close(SaveChanges=0)


def pdf_to_word(path, storage_path):
    p2w = Converter(path)
    _, old_filename = os.path.split(path)
    new_filename, _ = os.path.splitext(old_filename)
    new_path = os.path.join(storage_path, new_filename+'.docx')
    p2w.convert(new_path, start=0, end=None)
    p2w.close()
