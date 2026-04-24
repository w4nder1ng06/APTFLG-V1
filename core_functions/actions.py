import pyautogui
import time
import random
import pydirectinput
import pygetwindow as gw
from core_functions.vision import find_coord
def focus_game(window = None):
    try:
        windows = gw.getWindowsWithTitle(window)
        if windows:
            roblox_window = windows[0]
            roblox_window.activate()
            center_x = roblox_window.left + (roblox_window.width // 2)
            center_y = roblox_window.top + (roblox_window.height // 2)
            print("Roblox found! Targeting...")
            pyautogui.moveTo(center_x, center_y, duration=random.uniform(0.6, 1.4))
            pydirectinput.click(center_x, center_y)
            return True

    except Exception as e:
        print("Cannot find roblox! Aborting...")
    return False

def human_click(x, y, is_double=False):
    # Anti-cheat solution
    target_x = x + random.randint(-2, 2)
    target_y = y + random.randint(-2, 2)

    # Move to target
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.6, 1.4))
    time.sleep(0.2)
    pydirectinput.moveRel(random.randint(-1, 1), random.randint(-1, 1))

    if is_double:
        pydirectinput.doubleClick()
    else:
        pydirectinput.click()

def wait_and_click(image_path, timeout=30, double=False, window_name = None):
    start_time = time.time()
    while time.time() - start_time < timeout:
        found = find_coord(image_path, window_name = window_name)
        if found:
            x, y, conf = found
            print(f"Target {image_path} found! Clicking...")
            human_click(x, y, is_double=double)
            return True
        time.sleep(3)
    print(f"Timed out looking for {image_path}")
    return False

def scroll_n_find(target, threshold = 0.7, max_scroll = 10, window = None):
    if not focus_game(window=window):
        print("Cannot find game!")
        return None
    time.sleep(1)
    for i in range(max_scroll):
        found = find_coord(target, threshold, window_name=window)
        if found:
            print("Target game found!")
            return found
        print("Target game not found! Scrolling...")
        for _ in range(3):
            pydirectinput.press('down')
            time.sleep(1)

        time.sleep(1.5)
    return None