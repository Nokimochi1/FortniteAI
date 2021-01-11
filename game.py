import pydirectinput
import time
import pyautogui

class FindPath:

    def mapScreenshot(self):
        time.sleep(2)
        pydirectinput.press("m")
        time.sleep(0.5)
        pydirectinput.moveTo(1039, 405)
        time.sleep(0.5)
        for x in range(100):
            pyautogui.scroll(20)
        pydirectinput.moveTo(1528, 1035)
        fortnite_map = pyautogui.screenshot(region=(461,335, 1119-461, 949-335))
        fortnite_map.save("FortniteBot/screenshots/fortnitemap.png")


FindPath().mapScreenshot()