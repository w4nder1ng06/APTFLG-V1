import time
from core_functions.actions import wait_and_click
import config

def daily(game_name, assets):
    step1 = wait_and_click(assets["go_button"], timeout=30, window_name=game_name)
    time.sleep(1)
    step2 = wait_and_click(assets["claim_button"], timeout=30, window_name=game_name)
    time.sleep(1)
    step3 = wait_and_click(assets["quit_button"], timeout=30, window_name=game_name)
    time.sleep(1)
    step4 = wait_and_click(assets["mail_button"], timeout=30, window_name=game_name)
    time.sleep(1)
    step5 = wait_and_click(assets["claim_all_button"], timeout=30, window_name=game_name)
    time.sleep(1)
    step6 = wait_and_click(assets["quit_button"], timeout=30, window_name=game_name)

    return step1 and step2 and step3 and step4 and step5 and step6
