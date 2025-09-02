import pygame
import numpy as np
# ייבוא פונקציית הקונבולוציה
from scipy.signal import convolve2d

class Game:
    """
    מימוש משחק החיים של קונווי עם הדמיה באמצעות Pygame.

    Args:
        width (int): רוחב שדה המשחק בתאים.
        height (int): גובה שדה המשחק בתאים.
        cell_size (int): גודל תא אחד בפיקסלים.
    """
    def __init__(self, width: int, height: int, cell_size: int = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.random.choice([0, 1], size=(height, width))

        pygame.init()
        self.screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("משחק החיים של קונווי")

    def step(self):
        """
        מבצע צעד אחד בסימולציית משחק החיים באמצעות קונבולוציה.
        מתודה זו מהירה ופשוטה בהרבה מלולאות for.
        """
        # גרעין לספירת שכנים. 1 - שכן, 0 - התא עצמו.
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])

        # החל קונבולוציה. mode='same' מבטיח את אותו גודל,
        # boundary='wrap' מבטיח "עטיפה" סביב הקצוות.
        neighbors_count = convolve2d(self.grid, kernel, mode='same', boundary='wrap')

        # החל את כללי המשחק באמצעות מסכות בוליאניות של NumPy

        # תנאי 1: תא חי (self.grid == 1) שורד אם יש לו 2 או 3 שכנים.
        survivors = ((neighbors_count == 2) | (neighbors_count == 3)) & (self.grid == 1)

        # תנאי 2: תא מת (self.grid == 0) קם לתחייה אם יש לו בדיוק 3 שכנים.
        newborns = (neighbors_count == 3) & (self.grid == 0)

        # עדכן את השדה: תא יהיה חי אם הוא שרד או זה עתה נולד.
        self.grid = (survivors | newborns).astype(int)

    def draw(self):
        """
        מצייר את שדה המשחק על מסך Pygame.
        """
        self.screen.fill((20, 20, 40))  # רקע כחול כהה

        # מצא את הקואורדינטות של כל התאים החיים בבת אחת
        alive_cells = np.argwhere(self.grid == 1)

        # צייר רק תאים חיים
        for y, x in alive_cells:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (x * self.cell_size, y * self.cell_size,
                              self.cell_size - 1, self.cell_size - 1)) # -1 עבור רשת
        pygame.display.flip()

    def run(self):
        """
        מפעיל את לולאת המשחק הראשית.
        """
        running = True
        paused = False # הוסף אפשרות להשהות את המשחק
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.K_SPACE: # השהה בלחיצת מקש רווח
                    paused = not paused

            self.draw() # צייר תחילה כדי לראות את המצב ההתחלתי
            if not paused:
                self.step()

            clock.tick(10)  # הגבל ל-10 פריימים לשנייה

        pygame.quit()

if __name__ == '__main__':
    game = Game(width=80, height=60, cell_size=10)
    game.run()