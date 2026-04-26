import cv2
import numpy as np
import pyautogui
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    ctypes.windll.user32.SetProcessDPIAware()


def get_true_scale():
    width_phys = ctypes.windll.user32.GetSystemMetrics(0)
    width_logic, _ = pyautogui.size()
    return width_phys / width_logic


def find_coord(target_path, threshold=0.7, window_name=None):
    scale_factor = get_true_scale()
    template = cv2.imread(target_path)

    if template is None: return None

    screenshot = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    scales = np.linspace(0.8, 2.2, 20)
    best_match = None
    max_score = -1

    for s in scales:
        w = int(template.shape[1] * s)
        h = int(template.shape[0] * s)
        if h > frame.shape[0] or w > frame.shape[1]: continue
        res = cv2.matchTemplate(frame, cv2.resize(template, (w, h)), cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val > max_score:
            max_score = max_val
            phys_x = max_loc[0] + w // 2
            phys_y = max_loc[1] + h // 2
            best_match = (phys_x / scale_factor, phys_y / scale_factor, max_val)
            if max_val >= 0.9: break

    if max_score >= threshold:
        return best_match
    return None