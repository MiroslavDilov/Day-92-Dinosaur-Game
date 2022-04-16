from PIL import ImageGrab
import pyautogui
import time


pressed = 0
while True:
    screen = ImageGrab.grab()

    point = pyautogui.position()
    pos = point.x, point.y
    # print(screen.getpixel(pos))

    mouse_read = screen.getpixel(pos)

    if mouse_read == (83, 83, 83):
        pressed += 1
        # pyautogui.keyDown('space')
        # time.sleep(1)
        # pyautogui.keyUp('space')
        pyautogui.press("space")
        print(f"space_pressed: {pressed}")