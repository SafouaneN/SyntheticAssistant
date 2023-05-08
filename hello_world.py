from PIL import ImageGrab
import numpy as np
import cv2
import os
import pyautogui
import mouse

from mss import mss
from PIL import Image

import time

print("Hello, world!")
mouse.move(100, 100, absolute=False, duration=1.0)

bounding_box = {'top': 700, 'left': 0, 'width': 1000, 'height': 1000}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()

mouse.move(800,100,absolute=True, duration=0.2)
mouse.move(100,100,absolute=False, duration=1.0)
    
os.system("xdg-open example_file.txt")
time.sleep(3)
pyautogui.write('Hello There', interval = 0.1)
pyautogui.press('enter')
pyautogui.write('How is the Weather?', interval = 0.1)
pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')

print("Hello, Berlin!")
