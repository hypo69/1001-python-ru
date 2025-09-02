# **Amazin** (Maze Generator)

#### Description
The game is a maze generator that creates a unique maze with a single correct path each time. The player sets the dimensions of the maze, and the program builds it according to the specified parameters.

- **Features:**
  - The player enters the width and height of the maze.
  - The program guarantees a single path through the maze.
  - The maze is displayed on the screen.

---

### Step-by-step instructions for implementation:

#### 1. **Game Initialization**
   - Prompt the player to enter the maze dimensions (width and height).
   - Check that the entered dimensions are valid (e.g., greater than one).

#### 2. **Main Maze Generation Logic**
   - Create a matrix of the specified size, representing a grid of cells.
   - Use a maze generation algorithm, for example, *recursive depth-first search (DFS) algorithm*:
     - Start from a random initial cell.
     - Move to adjacent cells, removing walls between the current and next cell.
     - If all neighbors have been visited, backtrack to the previous cell and continue.
     - Complete the process when all cells have been visited.
   - Guarantee a single path through the maze.

#### 3. **Maze Display**
   - Use symbols for display:
     - `+`, `-`, `|` for walls.
     - Spaces for passages.
   - Output the generated maze in text format.

#### 4. **Additional Features**
   - Ability to set a preset size (e.g., 10x10) if the user entered invalid data.
   - Warning about excessively large maze sizes to prevent memory overload.

---

### Example of program execution

1. **Start**:
   ```
   Enter maze width and height:
   > 10 8
   ```

2. **Maze Output**:
   ```
   +--+--+--+--+--+--+--+--+--+--+
   |        |        |           |
   +  +--+  +  +--+  +  +--+--+  +
   |     |     |     |        |  |
   +--+  +  +--+  +  +  +--+  +  +
   |     |        |     |     |  |
   +--+--+--+--+--+--+--+--+--+--+
   ```

3. **Exit program**:
   ```
   Generate a new maze? (yes/no):
   > no
   Goodbye!
   ```

---