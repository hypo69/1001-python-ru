Inside the `game` directory, create a file `life.py`. 
Inside, write the implementation of Conway's "Game of Life" in Python, using an object-oriented approach.
Use libraries: `numpy`, `pygame` (for graphics).


Requirements:
1.  Create a `Game` class.
2.  In `__init__`, the class should accept grid dimensions (width, height) and create a random initial field.
3.  Create a `step()` method that updates the game state by one step according to the rules:
    - A living cell with < 2 living neighbors dies (loneliness).
    - A living cell with 2 or 3 living neighbors survives.
    - A living cell with > 3 living neighbors dies (overpopulation).
    - A dead cell with exactly 3 living neighbors becomes alive (birth).
4.  Create a `display()` method or override `__str__` to print the field to the console. Use characters, e.g., '■' for a living cell and ' ' for a dead one.
5.  Use the `numpy` library for efficient grid operations.
6.  In the `if __name__ == '__main__':` block, add an example that creates a game and runs the simulation in a loop with a small delay between steps.
7. For game visualization, use pygame or another graphics library, if possible.