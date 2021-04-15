from pynput.keyboard import Key, Controller
import time


keyboard = Controller()
time.sleep(3)
typethis = "Hello world"

x = 0

while x < 10:
    for char in typethis:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)
        x += 1
keyboard.press(Key.enter)
keyboard.release(Key.enter)
