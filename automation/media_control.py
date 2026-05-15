import time
import pyautogui


def play_in_app(song):

    # wait for app to fully open
    time.sleep(5)

    # bring app to focus
    pyautogui.click(600, 400)
    time.sleep(1)

    # try universal search shortcut
    pyautogui.hotkey('ctrl', 'l')  # works in many apps
    time.sleep(1)

    # fallback search shortcut
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(1)

    # type song
    pyautogui.write(song, interval=0.05)
    time.sleep(1)

    # press enter
    pyautogui.press('enter')
    time.sleep(3)

    # try play
    pyautogui.press('space')