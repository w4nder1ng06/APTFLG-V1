import time
import keyboard
import os
import config
from core_functions.actions import wait_and_click, scroll_n_find, human_click
from task_functions.MTD_Daily import daily
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


def quit_script():
    print("Quitting script...")
    os._exit(0)


def main():
    keyboard.add_hotkey("ctrl+q", quit_script)
    print("Available games: Roblox (1)")
    choice = input("Enter game key: ").strip()

    if choice not in config.ASSETS:
        print(f"Error: Game '{choice}' not found in config.py")
        return

    title_choice = config.ASSETS[choice]
    platform_data = title_choice["name"]
    if platform_data == "Roblox":
        print(f"Available {platform_data} games: {list(title_choice['sub_games'].keys())}")
        sub_choice = input("Enter the game key: ").strip()
        if sub_choice not in title_choice["sub_games"]:
            print(f"Error: Game '{sub_choice}' not found in config.py")
            return
        sub_game = title_choice["sub_games"][sub_choice]
        print(f"Bot is running for {choice}! You have 5 seconds...")
        time.sleep(5)

        if wait_and_click(title_choice["launcher"], double=True):
            print("Roblox launcher detected!")
            time.sleep(7)
            game_coord = scroll_n_find(sub_game["game_icon"], window=platform_data)

            if game_coord:
                human_click(game_coord[0], game_coord[1])
                time.sleep(3)

                if wait_and_click(sub_game["play_button"], timeout=30, window_name=platform_data):
                    print("In-game! Starting daily routine...")
                    time.sleep(10)
                    if daily(platform_data, sub_game):
                        print("Task completed!")
                    else:
                        print("Mission Failed: Daily routine interrupted.")
                else:
                    print("Timed out waiting for Play button.")
            else:
                print("Could not find the game icon in the scroll list.")
        else:
            print("Roblox launcher not found on desktop.")

    else:
        print("Game not supported yet! Stay tuned :b.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Global Error: {e}")
    input("\nPress ENTER to exit...")