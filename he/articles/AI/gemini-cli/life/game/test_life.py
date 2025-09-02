import numpy as np
from game.life import Game

def test_blinker_oscillation():
    """
    בודק את ההתפתחות הנכונה של מתנד "מהבהב".
    """
    # צור מופע של Game בגודל קבוע
    game = Game(width=5, height=5)

    # הגדר את המצב ההתחלתי של השדה: מהבהב אופקי
    initial_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    game.grid = initial_grid.copy()

    # מצב צפוי לאחר הצעד הראשון (מהבהב אנכי)
    expected_grid_step1 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # בצע את הצעד הראשון
    game.step()
    assert np.array_equal(game.grid, expected_grid_step1), "המהבהב לא עבר למצב אנכי לאחר הצעד הראשון"

    # בצע את הצעד השני
    game.step()
    assert np.array_equal(game.grid, initial_grid), "המהבהב לא חזר למצב אופקי לאחר הצעד השני"