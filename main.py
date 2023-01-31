"""
@author: 尼扣尼尼
@create time: 2023-1-31
@experience: 2.5 year
@version: 2.5
"""


import traceback
import os


def main():
    if not os.environ.get('PICTURE_PATH', None):
        picture_path = os.path.join(os.getcwd(), 'pic')
        os.environ.setdefault('PICTURE_PATH', picture_path)
    if not os.environ.get('VIDEO_PATH', None):
        video_path = os.path.join(os.getcwd(), 'video')
        os.environ.setdefault('VIDEO_PATH', video_path)
    try:
        from gegezhuanhuanqi.window import window
        window()
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    main()
