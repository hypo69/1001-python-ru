# Project "Game of Life"

## Brief description

This project is an implementation of Conway's "Game of Life" cellular automaton in Python. The game simulates the evolution of a cell population on a two-dimensional grid, where the state of each cell (alive or dead) changes depending on the state of its neighbors.

## File structure

-   `life.py`: The main file containing the implementation of the `Game` class, which manages the logic of the "Game of Life" simulation and its graphical visualization using the `pygame` library.
-   `test_life.py`: A file with unit tests for the `Game` class, using the `pytest` framework. Includes a test to check the evolution of the "Blinker" oscillator.

## How to run the simulation

To run the "Game of Life" simulation, make sure you have the necessary libraries (`numpy` and `pygame`) installed. If not, install them:

```bash
pip install numpy pygame
```

Then run the main file:

```bash
python game/life.py
```

## How to run tests

To run tests, you need to install `pytest` and `numpy`:

```bash
pip install pytest numpy
```

Then run the tests, specifying the path to the test file:

```bash
pytest game/test_life.py
```