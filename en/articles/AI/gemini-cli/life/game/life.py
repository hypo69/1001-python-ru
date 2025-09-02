import pygame
import numpy as np
# Import the convolution function
from scipy.signal import convolve2d

class Game:
    """
    Implementation of Conway's Game of Life with Pygame visualization.

    Args:
        width (int): Width of the game field in cells.
        height (int): Height of the game field in cells.
        cell_size (int): Size of one cell in pixels.
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
        Performs one step of the Game of Life simulation using convolution.
        This method is much faster and simpler than for loops.
        """
        # Kernel for counting neighbors. 1 - neighbor, 0 - the cell itself.
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        
        # Apply convolution. mode='same' ensures the same size,
        # boundary='wrap' ensures "wrapping" around the edges.
        neighbors_count = convolve2d(self.grid, kernel, mode='same', boundary='wrap')
        
        # Apply game rules using NumPy boolean masks
        
        # Condition 1: A living cell (self.grid == 1) survives if it has 2 or 3 neighbors.
        survivors = ((neighbors_count == 2) | (neighbors_count == 3)) & (self.grid == 1)
        
        # Condition 2: A dead cell (self.grid == 0) comes to life if it has exactly 3 neighbors.
        newborns = (neighbors_count == 3) & (self.grid == 0)
        
        # Update the field: a cell will be alive if it survived OR just born.
        self.grid = (survivors | newborns).astype(int)

    def draw(self):
        """
        Draws the game field on the Pygame screen.
        """
        self.screen.fill((20, 20, 40))  # Dark blue background
        
        # Find the coordinates of all living cells at once
        alive_cells = np.argwhere(self.grid == 1)
        
        # Draw only living cells
        for y, x in alive_cells:
            pygame.draw.rect(self.screen, (255, 255, 255), 
                             (x * self.cell_size, y * self.cell_size, 
                              self.cell_size - 1, self.cell_size - 1)) # -1 for grid
        pygame.display.flip()

    def run(self):
        """
        Starts the main game loop.
        """
        running = True
        paused = False # Add ability to pause the game
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.K_SPACE: # Pause on spacebar press
                    paused = not paused

            self.draw() # Draw first to see initial state
            if not paused:
                self.step()
            
            clock.tick(10)  # Limit to 10 frames per second

        pygame.quit()

if __name__ == '__main__':
    game = Game(width=80, height=60, cell_size=10)
    game.run()