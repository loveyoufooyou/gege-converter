from gegezhuanhuanqi.buttons import Buttonn
from gegezhuanhuanqi.center import Root
from gegezhuanhuanqi.frame import Framee
from gegezhuanhuanqi.label import Labell
from gegezhuanhuanqi.lst import ListBox
from gegezhuanhuanqi.menu import Menuu


def window():
    # root window and listbox-left (window)
    root = Root()
    list_box = ListBox(root)

    # frame-main-left (container)
    frame_main = Framee(root)
    frame_main.add_main()

    # frame-sub-top (button)
    frame_top = Framee(frame_main.frame)
    frame_top.add()
    btn = Buttonn(frame_top.frame, list_box)

    # frame-sub-top (picture)
    frame_bottom = Framee(frame_main.frame)
    frame_bottom.add()
    lab = Labell(frame_bottom.frame)

    menu = Menuu(root, btn)
    root.bind('<ButtonPress-3>', menu.show)
    root.mainloop()
