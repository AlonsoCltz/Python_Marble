# Pachinko Marble Game

A classic Pachinko-style marble game built with Python, featuring physics-based mechanics and an interactive UI. The objective is to launch marbles and have them land in winning slots to increase your score.

![Gameplay Screenshot](imageim.png) 
*(You can replace `imageim.png` with an actual screenshot of your game)*

## Table of Contents
- [Features](#features)
- [Gameplay](#gameplay)
- [Technical Details](#technical-details)
- [Libraries](#libraries)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Building an Executable](#building-an-executable)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Features
- **Physics-Based Engine**: Utilizes a simple physics model for gravity and realistic marble bouncing.
- **Interactive Launch System**: A UI slider controls the number of marbles to bet, and a dynamic power meter sets the launch strength.
- **Dynamic Game Board**: The board is populated with a grid of pillars (pegs) for the marbles to bounce off.
- **Scoring System**: Win or lose marbles based on where your marble lands.
- **Graphical Interface**: Built with `pygame` for the main game window and `tkinter` for user input dialogs.

## Gameplay
The game is a digital version of Pachinko. You start with a set number of marbles. Before each launch, you decide how many marbles to risk. You then control the launch power to guide the marble through a field of pegs. If the marble lands in a designated winning slot at the bottom, you win back the marbles you risked, plus a bonus. If it lands in a losing slot, you lose the marbles. The game ends when you run out of marbles.

## Technical Details
The core physics is handled by a `bounce` function that calculates the resulting velocity vector of the marble after colliding with an object. It uses vector projection to simulate the collision response. The game loop continuously applies gravity and updates the marble's position, checking for collisions with pegs and boundary walls.

## Libraries
This project relies on the following Python libraries:
- **Pygame**: For handling graphics, game loops, and user input.
- **Tkinter**: For creating the initial UI dialog to select the number of marbles.

## Prerequisites
- Python 3.x
- `pip` (Python package installer)

## Installation
1.  Clone the repository or download the source code.
2.  Navigate to the project directory in your terminal.
3.  Install the required packages:
    ```powershell
    pip install pygame
    ```

## How to Play
1.  Run the game from the terminal:
    ```powershell
    python main.py
    ```
2.  A dialog window will appear. Use the slider to select the number of marbles you want to play in this round and press **"save"**.
3.  In the main game window, a white bar will start moving left and right at the bottom. This is the power meter.
4.  **Click the mouse** to launch the marble. The position of the power meter at the time of your click determines the launch velocity.
5.  Watch the marble fall through the pegs. If it lands in a red-colored slot at the bottom, you win!
6.  The game will automatically reset for the next round. The game ends if you lose all your marbles.

## Building an Executable
You can create a standalone executable file using PyInstaller, which bundles the game and its dependencies.

1.  Install PyInstaller:
    ```powershell
    pip install pyinstaller
    ```
2.  Run the build command from the terminal. The included `.spec` file is already configured.
    ```powershell
    pyinstaller main.spec
    ```
    Alternatively, you can use the command found in `main.py`:
    ```powershell
    pyinstaller -F -w -i ./icicic.ico main.py
    ```
3.  The executable will be located in the `dist/` directory.

## File Structure
```
.
├── main.py           # Main game logic, rendering, and physics
├── iquery.py         # A small tkinter test script (not used in the main game)
├── main.spec         # PyInstaller build configuration
├── icicic.ico        # Icon file for the executable
├── imageim.png       # Gameplay image
└── README.md         # This file
```