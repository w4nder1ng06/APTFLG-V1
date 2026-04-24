**APTFLG-V1 (All Purpose Tool For Lazy Gamers)

A simple tool built with images matching so you can build your simple bot that do simple tasks for you.
Currently, it supports the game called "Merge Tower Defense" in "Roblox", it will automatically open Roblox, join the game for you and claim the daily collectibles (Mining, Ranked prize via mail).

**Key Features

+Multiscale Vision Engine**: Utilizes OpenCV template matching with dynamic scaling (0.4x to 1.6x) to ensure reliable icon detection across various screen resolutions and DPI settings.
+Modular Architecture**: Clean separation of concerns between core logic (`core_functions`), game-specific routines (`task_functions`), and centralized data (`config.py`).
+Anti-Cheat & Stealth**:
    -->Human-like Interaction**: Implements randomized click offsets and variable movement durations to mimic human input patterns.
    -->Driver-Level Input**: Uses `pydirectinput` for hardware-level mouse and keyboard emulation, bypassing standard software-based detection.
+Resource Optimization**: Employs region-specific screen capturing to minimize CPU/GPU load during image processing.
+Configuration-Driven**: Zero hardcoded paths. All asset locations, thresholds, and platform hierarchies are managed via a centralized configuration file.
+Multi-Platform Ready**: Designed to support various launchers (Roblox, Steam, etc.) through a hierarchical dispatcher.

**Known issue: It is still pretty slow, but I will fix it soon if I have time, you should always run roblox in full-screen mode to ensure best result, of course it supports different sized windows, but I cannot guarantee the bot will run if the window is too small or too large.

EXPECT UPDATES :)!
