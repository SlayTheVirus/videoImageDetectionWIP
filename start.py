import pyautogui
import time

pic = pyautogui.screenshot()
size = pyautogui.size()
mousepos = pyautogui.postion()

# Wait 5 secs and then take a screenshot
time.sleep(5)
pic.save('/temp/screen.jpg')
