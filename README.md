# Pygame Snake Game

A classic Snake game implemented using the Pygame library in Python.

![Game Screenshot](assets/images/screenshot.png)
![Gameplay GIF](assets/images/gameplay.gif)

## Description

This repository contains the source code for a simple and engaging Snake game built with Pygame. Players control a snake, navigating it to eat food and grow longer while avoiding collisions with the walls and its own body. The game features a welcome screen with background music, in-game music to enhance the experience, score tracking with a persistent high score, and a distinct game over screen with a sound effect.

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [How to Play](#how-to-play)
* [Game Elements](#game-elements)
* [Libraries Used](#libraries-used)
* [File Structure](#file-structure)
* [Screenshots](#screenshots)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)

## Features

* **Classic Snake Gameplay:** Enjoy the familiar and addictive Snake game mechanics.
* **Score Tracking:** Keep track of your current score during the game.
* **Persistent High Score:** The highest score achieved is saved in a file (`hiscore.txt`) and persists across game sessions.
* **Welcome Screen:** An introductory screen with the game title and instructions to start. Features background music (`bgm.mp3`).
* **In-Game Music:** Engaging background music (`bgm1.mp3`) plays during the gameplay.
* **Game Over Screen:** A clear "Game Over" screen with an image and instructions to play again. Features a distinct sound effect (`end.mp3`).
* **Boundary Detection:** The game ends if the snake hits the edges of the game window.
* **Self-Collision Detection:** The game ends if the snake collides with its own body.
* **Random Food Generation:** Food appears randomly within the game window.
* **Increasing Difficulty (Implicit):** As the snake grows longer, the game becomes progressively more challenging.
* **Clear Visuals:** Utilizes Pygame's drawing capabilities for a simple and effective visual representation.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ahmadrazaumair008/Snake-game/edit/main/README.md]
    cd pygame-snake-game
    ```

2.  **Install Pygame:**
    If you don't have Pygame installed, you can install it using pip:
    ```bash
    pip install pygame
    ```

3.  **Ensure Assets are Present:**
    Make sure the following files are in the same directory as your `snake_game.py` script (or in the specified `assets` subdirectories as shown in the [File Structure](#file-structure) section):
    * `bg.jpg` (Background image)
    * `INTRO.png` (Intro screen image)
    * `GAMEOVER.png` (Game over screen image)
    * `bgm.mp3` (Welcome screen music)
    * `bgm1.mp3` (In-game music)
    * `end.mp3` (Game over sound effect)

## How to Play

1.  Run the game by executing the Python script:
    ```bash
    python snake_game.py
    ```

2.  **Welcome Screen:**
    * The game will start with a welcome screen displaying the title.
    * Press the **ENTER** key to begin playing the game.

3.  **Gameplay:**
    * Use the **arrow keys** to control the direction of the snake:
        * **Up Arrow:** Move the snake upwards.
        * **Down Arrow:** Move the snake downwards.
        * **Left Arrow:** Move the snake to the left.
        * **Right Arrow:** Move the snake to the right.
    * The goal is to navigate the snake to eat the red food.
    * Each time the snake eats food, it grows longer, and your score increases by 10.
    * Avoid colliding with the walls of the game window or the snake's own body. If a collision occurs, the game will end.

4.  **Game Over Screen:**
    * When the game ends, a "Game Over" screen will be displayed.
    * Press the **SPACE** key to return to the welcome screen and play a new game.

## Game Elements

* **Snake:** Controlled by the player, represented by black rectangles.
* **Food:** Represented by a red rectangle. Eating it makes the snake grow and increases the score.
* **Walls:** The boundaries of the game window. Colliding with them ends the game.
* **Score:** The current score achieved during the game, displayed at the top-left.
* **High Score:** The highest score achieved across all game sessions, also displayed at the top-left.

## Libraries Used

* **Pygame:** A free and open-source cross-platform library for the creation of multimedia applications like video games.

## File Structure
