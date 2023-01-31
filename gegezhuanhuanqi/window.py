from gegezhuanhuanqi.buttons import Buttonn
from gegezhuanhuanqi.center import Root
from gegezhuanhuanqi.frame import Framee
from gegezhuanhuanqi.label import Labell
from gegezhuanhuanqi.lst import ListBox
from gegezhuanhuanqi.menu import Menuu


def window():
    # root window and listbox-left (window)
    root = Root()
    menu = Menuu(root)
    root.bind('<ButtonPress-3>', menu.show)
    list_box = ListBox(root)

    # frame-main-left (container)
    frame_main = Framee(root)
    frame_main.add_main()

    # frame-sub-top (button)
    frame_top = Framee(frame_main.frame)
    frame_top.add()
    btn = Buttonn(frame_top.frame)
    btn.add_delete(list_box)
    btn.add_clear(list_box)
    btn.add_word_to_pdf(list_box)
    btn.add_pdfs_to_pdf(list_box)
    btn.add_imgs_to_pdf(list_box)

    # frame-sub-top (picture)
    frame_bottom = Framee(frame_main.frame)
    frame_bottom.add()
    lab = Labell(frame_bottom.frame)
    root.mainloop()


