
import numpy as np
from game.life import Game

def test_blinker_oscillation():
    """
    Проверяет правильность эволюции осциллятора "Блинкер".
    """
    # Создаем экземпляр Game с фиксированным размером
    game = Game(width=5, height=5)

    # Устанавливаем начальное состояние поля: горизонтальный блинкер
    initial_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    game.grid = initial_grid.copy()

    # Ожидаемое состояние после первого шага (вертикальный блинкер)
    expected_grid_step1 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # Выполняем первый шаг
    game.step()
    assert np.array_equal(game.grid, expected_grid_step1), "Блинкер не перешел в вертикальное состояние после первого шага"

    # Выполняем второй шаг
    game.step()
    assert np.array_equal(game.grid, initial_grid), "Блинкер не вернулся в горизонтальное состояние после второго шага"
