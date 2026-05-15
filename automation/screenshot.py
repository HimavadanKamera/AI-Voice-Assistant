import pyautogui

from datetime import datetime

def take_screenshot():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()

    screenshot.save(filename)

    return filename