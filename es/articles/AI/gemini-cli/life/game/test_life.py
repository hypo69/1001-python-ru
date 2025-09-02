import numpy as np
from game.life import Game

def test_blinker_oscillation():
    """
    Comprueba la correcta evolución del oscilador "Blinker".
    """
    # Crea una instancia de Game con un tamaño fijo
    game = Game(width=5, height=5)

    # Establece el estado inicial del campo: parpadeo horizontal
    initial_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    game.grid = initial_grid.copy()

    # Estado esperado después del primer paso (parpadeo vertical)
    expected_grid_step1 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # Realiza el primer paso
    game.step()
    assert np.array_equal(game.grid, expected_grid_step1), "El parpadeo no cambió a estado vertical después del primer paso"

    # Realiza el segundo paso
    game.step()
    assert np.array_equal(game.grid, initial_grid), "El parpadeo no volvió a su estado horizontal después del segundo paso"