import pyautogui
from PIL import ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(s):
    for i in range(260, 415):
        for j in range(350, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 420):
        for j in range(600,705):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
