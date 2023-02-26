from pywebio.input import *
from pywebio.output import *
import webbrowser
import time

def play_video():
    url = input("Ссылка на видео：", type=TEXT)
    dur = input("Время просмотра (в секундах)：", type=NUMBER)
    wtc = input("Кол-во просмотров：", type=NUMBER)

    for i in range(wtc):
        webbrowser.open_new(url)
        time.sleep(dur)

if __name__ == '__main__':
    play_video()
