import pygame
import numpy as np
# Importar la función de convolución
from scipy.signal import convolve2d

class Game:
    """
    Implementación del Juego de la Vida de Conway con visualización Pygame.

    Args:
        width (int): Ancho del campo de juego en celdas.
        height (int): Alto del campo de juego en celdas.
        cell_size (int): Tamaño de una celda en píxeles.
    """
    def __init__(self, width: int, height: int, cell_size: int = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.random.choice([0, 1], size=(height, width))
        
        pygame.init()
        self.screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Juego de la Vida de Conway")

    def step(self):
        """
        Realiza un paso de la simulación del Juego de la Vida usando convolución.
        Este método es mucho más rápido y simple que los bucles for.
        """
        # Kernel para contar vecinos. 1 - vecino, 0 - la propia celda.
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        
        # Aplicar convolución. mode='same' asegura el mismo tamaño,
        # boundary='wrap' asegura el "envoltorio" alrededor de los bordes.
        neighbors_count = convolve2d(self.grid, kernel, mode='same', boundary='wrap')
        
        # Aplicar reglas del juego usando máscaras booleanas de NumPy
        
        # Condición 1: Una celda viva (self.grid == 1) sobrevive si tiene 2 o 3 vecinos.
        survivors = ((neighbors_count == 2) | (neighbors_count == 3)) & (self.grid == 1)
        
        # Condición 2: Una celda muerta (self.grid == 0) cobra vida si tiene exactamente 3 vecinos.
        newborns = (neighbors_count == 3) & (self.grid == 0)
        
        # Actualizar el campo: una celda estará viva si sobrevivió O acaba de nacer.
        self.grid = (survivors | newborns).astype(int)

    def draw(self):
        """
        Dibuja el campo de juego en la pantalla de Pygame.
        """
        self.screen.fill((20, 20, 40))  # Fondo azul oscuro
        
        # Encontrar las coordenadas de todas las celdas vivas a la vez
        alive_cells = np.argwhere(self.grid == 1)
        
        # Dibujar solo las celdas vivas
        for y, x in alive_cells:
            pygame.draw.rect(self.screen, (255, 255, 255), 
                             (x * self.cell_size, y * self.cell_size, 
                              self.cell_size - 1, self.cell_size - 1)) # -1 para la cuadrícula
        pygame.display.flip()

    def run(self):
        """
        Inicia el bucle principal del juego.
        """
        running = True
        paused = False # Añadir la capacidad de pausar el juego
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.K_SPACE: # Pausar al presionar la barra espaciadora
                    paused = not paused

            self.draw() # Dibujar primero para ver el estado inicial
            if not paused:
                self.step()
            
            clock.tick(10)  # Limitar a 10 fotogramas por segundo

        pygame.quit()

if __name__ == '__main__':
    game = Game(width=80, height=60, cell_size=10)
    game.run()