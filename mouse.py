import pyautogui
import time


pyautogui.keyUp('d')
time.sleep(3)
print('run')
pyautogui.keyDown('a')
time.sleep(.5)
pyautogui.keyUp('a')