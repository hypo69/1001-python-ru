import pygame
import numpy as np
# Importer la fonction de convolution
from scipy.signal import convolve2d

class Game:
    """
    Implémentation du Jeu de la Vie de Conway avec visualisation Pygame.

    Args:
        width (int): Largeur du champ de jeu en cellules.
        height (int): Hauteur du champ de jeu en cellules.
        cell_size (int): Taille d'une cellule en pixels.
    """
    def __init__(self, width: int, height: int, cell_size: int = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.random.choice([0, 1], size=(height, width))
        
        pygame.init()
        self.screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Jeu de la Vie de Conway")

    def step(self):
        """
        Exécute une étape de la simulation du Jeu de la Vie en utilisant la convolution.
        Cette méthode est beaucoup plus rapide et simple que les boucles for.
        """
        # Noyau pour compter les voisins. 1 - voisin, 0 - la cellule elle-même.
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        
        # Appliquer la convolution. mode='same' garantit la même taille,
        # boundary='wrap' assure un "enroulement" sur les bords.
        neighbors_count = convolve2d(self.grid, kernel, mode='same', boundary='wrap')
        
        # Appliquer les règles du jeu à l'aide de masques booléens NumPy
        
        # Condition 1: Une cellule vivante (self.grid == 1) survit si elle a 2 ou 3 voisins.
        survivors = ((neighbors_count == 2) | (neighbors_count == 3)) & (self.grid == 1)
        
        # Condition 2: Une cellule morte (self.grid == 0) prend vie si elle a exactement 3 voisins.
        newborns = (neighbors_count == 3) & (self.grid == 0)
        
        # Mettre à jour le champ: une cellule sera vivante si elle a survécu OU vient de naître.
        self.grid = (survivors | newborns).astype(int)

    def draw(self):
        """
        Dessine le champ de jeu sur l'écran Pygame.
        """
        self.screen.fill((20, 20, 40))  # Fond bleu foncé
        
        # Trouver les coordonnées de toutes les cellules vivantes en une seule fois
        alive_cells = np.argwhere(self.grid == 1)
        
        # Dessiner uniquement les cellules vivantes
        for y, x in alive_cells:
            pygame.draw.rect(self.screen, (255, 255, 255), 
                             (x * self.cell_size, y * self.cell_size, 
                              self.cell_size - 1, self.cell_size - 1)) # -1 pour la grille
        pygame.display.flip()

    def run(self):
        """
        Démarre la boucle de jeu principale.
        """
        running = True
        paused = False # Ajouter la possibilité de mettre le jeu en pause
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.K_SPACE: # Pause sur la touche espace
                    paused = not paused

            self.draw() # Dessiner d'abord pour voir l'état initial
            if not paused:
                self.step()
            
            clock.tick(10)  # Limiter à 10 images par seconde

        pygame.quit()

if __name__ == '__main__':
    game = Game(width=80, height=60, cell_size=10)
    game.run()