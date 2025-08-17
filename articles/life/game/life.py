import pygame
import numpy as np
# Импортируем функцию для свёртки
from scipy.signal import convolve2d

class Game:
    """
    Реализация игры "Жизнь" Конвея с визуализацией на Pygame.

    Args:
        width (int): Ширина игрового поля в клетках.
        height (int): Высота игрового поля в клетках.
        cell_size (int): Размер одной клетки в пикселях.
    """
    def __init__(self, width: int, height: int, cell_size: int = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.random.choice([0, 1], size=(height, width))
        
        pygame.init()
        self.screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Conway's Game of Life")

    def step(self):
        """
        Выполняет один шаг симуляции игры "Жизнь" с использованием свёртки.
        Этот метод намного быстрее и проще, чем циклы for.
        """
        # Ядро для подсчета соседей. 1 - сосед, 0 - сама клетка.
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        
        # Применяем свёртку. mode='same' гарантирует тот же размер,
        # boundary='wrap' обеспечивает "заворачивание" по краям.
        neighbors_count = convolve2d(self.grid, kernel, mode='same', boundary='wrap')
        
        # Применяем правила игры с помощью булевых масок NumPy
        
        # Условие 1: Живая клетка (self.grid == 1) выживает, если у нее 2 или 3 соседа.
        survivors = ((neighbors_count == 2) | (neighbors_count == 3)) & (self.grid == 1)
        
        # Условие 2: Мертвая клетка (self.grid == 0) оживает, если у нее ровно 3 соседа.
        newborns = (neighbors_count == 3) & (self.grid == 0)
        
        # Обновляем поле: клетка будет жива, если она выжила ИЛИ только что родилась.
        self.grid = (survivors | newborns).astype(int)

    def draw(self):
        """
        Отрисовывает игровое поле на экране Pygame.
        """
        self.screen.fill((20, 20, 40))  # Темно-синий фон
        
        # Находим координаты всех живых клеток за один раз
        alive_cells = np.argwhere(self.grid == 1)
        
        # Отрисовываем только живые клетки
        for y, x in alive_cells:
            pygame.draw.rect(self.screen, (255, 255, 255), 
                             (x * self.cell_size, y * self.cell_size, 
                              self.cell_size - 1, self.cell_size - 1)) # -1 для сетки
        pygame.display.flip()

    def run(self):
        """
        Запускает основной цикл игры.
        """
        running = True
        paused = False # Добавим возможность ставить игру на паузу
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # Пауза по нажатию на пробел
                        paused = not paused

            self.draw() # Рисуем сначала, чтобы видеть начальное состояние
            if not paused:
                self.step()
            
            clock.tick(10)  # Ограничение до 10 кадров в секунду

        pygame.quit()

if __name__ == '__main__':
    game = Game(width=80, height=60, cell_size=10)
    game.run()