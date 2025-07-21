import random
import time
import os

def create_grid(rows, cols):
    """Creates an empty grid."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def initialize_grid(grid, density=0.2):
    """Initializes the grid with random live cells."""
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if random.random() < density:
                grid[r][c] = 1
            else:
                grid[r][c] = 0
    return grid

def display_grid(grid):
    """Clears the console and displays the grid."""
    os.system('cls' if os.name == 'nt' else 'clear') # Clear console
    for row in grid:
        print(" ".join(["■" if cell == 1 else "□" for cell in row]))

def count_neighbors(grid, r, c):
    """Counts live neighbors for a cell."""
    rows = len(grid)
    cols = len(grid[0])
    live_neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nr, nc = r + i, c + j
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                live_neighbors += 1
    return live_neighbors

def update_grid(grid):
    """Applies the rules of the Game of Life to update the grid."""
    rows = len(grid)
    cols = len(grid[0])
    new_grid = create_grid(rows, cols)

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1:  # Live cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[r][c] = 0  # Dies
                else:
                    new_grid[r][c] = 1  # Lives
            else:  # Dead cell
                if neighbors == 3:
                    new_grid[r][c] = 1  # Becomes alive
                else:
                    new_grid[r][c] = 0  # Stays dead
    return new_grid

def main():
    rows = 20
    cols = 40
    generations = 100

    grid = create_grid(rows, cols)
    grid = initialize_grid(grid)

    print("Starting Conway's Game of Life...")
    time.sleep(2)

    for gen in range(generations):
        display_grid(grid)
        print(f"Generation: {gen + 1}")
        grid = update_grid(grid)
        time.sleep(0.1) # Adjust for faster/slower simulation

    print("\nSimulation finished.")

if __name__ == "__main__":
    main()
