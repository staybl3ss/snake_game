Snake Game

The classic Snake game built with Python using object-oriented programming principles. This is one of the first games I had coded up in Python, and I decided
to create something that I had played as a kid. The logic behind this was to use the turtle module to create "living" icons that could listen to user input and
act similar to sprites in a game. Every time the snake eats food, it will grow by appending new turtle objects to the snake's body length. The end-goal of the game is to get the highest score you can before dying.

# Goal

The purpose of this project was to practice:
- Object-Oriented Programming (OOP)
- Game loop logic
- Handling user input and transmitting it to a visual display
- Using Python's `turtle` module for graphics

# Core Logic

- The game consists of a snake that moves continuously in the last direction it was steered. It begins with a length of 3.
- The player controls the snake using arrow keys, it moves forward automatically.
- Every time the snake eats food, the snake grows longer by 1 unit.
- If the snake runs into the wall or into its own body, then the game is Over.

# Features

- Score tracking / scoreboard
- Food spawning at random locations on the two-dimensional plane
- Game-over logic on wall collision or self-collision
- Snake body and growth formed using a list of turtle segments


# Concepts Used

- Classes and objects (Snake, Food, Scoreboard)
- Loops and conditionals (using game logic)
- Collision detection
- Keyboard event handling by Listening to Userr Input on the Keyboard
