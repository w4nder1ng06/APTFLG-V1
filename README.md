**APTFLG-V1 (All Purpose Tool For Lazy Gamers)

A simple tool built with images matching so you can build your simple bot that do simple tasks for you.

**Key Features

+Multiscale Vision Engine**: Utilizes OpenCV template matching with dynamic scaling (0.4x to 1.6x) to ensure reliable icon detection across various screen resolutions and DPI settings.
+Modular Architecture**: Clean separation of concerns between core logic (`core_functions`), game-specific routines (`task_functions`), and centralized data (`config.py`).
+Anti-Cheat & Stealth**:
    -->Human-like Interaction**: Implements randomized click offsets and variable movement durations to mimic human input patterns.
    -->Driver-Level Input**: Uses `pydirectinput` for hardware-level mouse and keyboard emulation, bypassing standard software-based detection.
+Resource Optimization**: Employs region-specific screen capturing to minimize CPU/GPU load during image processing.
+Configuration-Driven**: Zero hardcoded paths. All asset locations, thresholds, and platform hierarchies are managed via a centralized configuration file.
+Multi-Platform Ready**: Designed to support various launchers (Roblox, Steam, etc.) through a hierarchical dispatcher.

**Project Structure

APTFLG-V1/
├── main.py                 
├── config.py               
├── core_functions/
│   ├── vision.py           
│   └── actions.py          
├── task_functions/
│   └── MTD_Daily.py        
└── targets/                
