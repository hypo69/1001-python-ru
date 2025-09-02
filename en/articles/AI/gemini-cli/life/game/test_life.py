import numpy as np
from game.life import Game

def test_blinker_oscillation():
    """
    Checks the correct evolution of the "Blinker" oscillator.
    """
    # Create a Game instance with a fixed size
    game = Game(width=5, height=5)

    # Set the initial state of the field: horizontal blinker
    initial_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    game.grid = initial_grid.copy()

    # Expected state after the first step (vertical blinker)
    expected_grid_step1 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # Perform the first step
    game.step()
    assert np.array_equal(game.grid, expected_grid_step1), "Blinker did not transition to vertical state after first step"

    # Perform the second step
    game.step()
    assert np.array_equal(game.grid, initial_grid), "Blinker did not return to horizontal state after second step"