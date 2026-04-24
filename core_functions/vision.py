import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

def find_coord(target_path, threshold = 0.7, window_name = None):
    template = cv2.imread(target_path)
    if template is None:
        return None
    offset_x, offset_y = 0, 0
    region = None
    if window_name:
        try:
            win = gw.getWindowsWithTitle(window_name)[0]
            # Define the region: (left, top, width, height)
            region = (win.left, win.top, win.width, win.height)
            offset_x, offset_y = win.left, win.top
        except:
            return None
    scales = np.linspace(0.4, 1.6, 30)
    screenshot = np.array(pyautogui.screenshot(region=region))
    frame = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    best_match = None
    max_score = -1
    for scale in scales:
        width = int(template.shape[1] * scale)
        height = int(template.shape[0] * scale)
        resized_template = cv2.resize(template, (width, height))
        if height > frame.shape[0] or width > frame.shape[1]:
            continue
        result = cv2.matchTemplate(frame, resized_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_score < max_val:
            max_score = max_val
            best_match = (max_loc[0] + width//2 + offset_x, max_loc[1] + height//2 + offset_y, max_val)
            if max_val >= 0.9:
                return best_match
    if max_score >= threshold:
        return best_match
    return None

