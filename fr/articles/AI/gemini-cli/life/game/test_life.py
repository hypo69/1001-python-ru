import numpy as np
from game.life import Game

def test_blinker_oscillation():
    """
    Vérifie la bonne évolution de l'oscillateur "Blinker".
    """
    # Crée une instance de Game avec une taille fixe
    game = Game(width=5, height=5)

    # Définit l'état initial du champ : clignotant horizontal
    initial_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    game.grid = initial_grid.copy()

    # État attendu après la première étape (clignotant vertical)
    expected_grid_step1 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # Exécute la première étape
    game.step()
    assert np.array_equal(game.grid, expected_grid_step1), "Le clignotant n'est pas passé à l'état vertical après la première étape"

    # Exécute la deuxième étape
    game.step()
    assert np.array_equal(game.grid, initial_grid), "Le clignotant n'est pas revenu à l'état horizontal après la deuxième étape"