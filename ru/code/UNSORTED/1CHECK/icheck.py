"""
Checkerboard Puzzle Solver

Rules of the Puzzle:
1. The board is an 8x8 grid (standard checkerboard).
2. Initially, 48 checkers are placed on the two outermost rows (rows 1 and 8).
3. Checkers can only move diagonally.
4. A checker can "jump" over an adjacent checker diagonally if the landing square is empty.
5. The jumped checker is removed from the board.
6. The objective is to remove as many checkers as possible by performing valid jumps.
7. The game ends when no more valid jumps are possible.
"""

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Checkerboard:
    """
    Represents the checkerboard and its state.
    """
    board: List[List[int]]  # 0 = empty, 1 = checker
    removed_checkers: int = 0  # Counter for removed checkers

    def __post_init__(self) -> None:
        """
        Initialize the board with 48 checkers on the outermost rows.
        """
        for row in [0, 7]:  # Rows 1 and 8 (0-indexed)
            for col in range(8):
                self.board[row][col] = 1

    def is_valid_jump(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        """
        Check if a jump is valid.
        Rules:
        - The landing position must be within the board.
        - The landing position must be empty.
        - There must be a checker to jump over.
        - The jump must be diagonal (2 squares in row and column).

        :param start: Tuple (row, col) of the starting position.
        :param end: Tuple (row, col) of the landing position.
        :return: True if the jump is valid, False otherwise.
        """
        start_row, start_col = start
        end_row, end_col = end

        # Check if the landing position is within the board
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Check if the landing position is empty
        if self.board[end_row][end_col] != 0:
            return False

        # Calculate the middle position (the jumped checker)
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2

        # Check if there is a checker to jump over
        if self.board[mid_row][mid_col] != 1:
            return False

        # Check if the jump is diagonal
        if abs(start_row - end_row) != 2 or abs(start_col - end_col) != 2:
            return False

        return True

    def perform_jump(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Perform a jump and remove the jumped checker.
        Rules:
        - Move the checker from the start position to the end position.
        - Remove the checker in the middle position.
        - Increment the count of removed checkers.

        :param start: Tuple (row, col) of the starting position.
        :param end: Tuple (row, col) of the landing position.
        """
        start_row, start_col = start
        end_row, end_col = end

        # Move the checker
        self.board[start_row][start_col] = 0
        self.board[end_row][end_col] = 1

        # Remove the jumped checker
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        self.board[mid_row][mid_col] = 0

        # Increment the removed checkers count
        self.removed_checkers += 1

    def find_possible_jumps(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """
        Find all possible jumps on the board.
        Rules:
        - Scan the board for checkers.
        - For each checker, check all four diagonal directions for valid jumps.

        :return: List of tuples, where each tuple contains (start, end) positions for valid jumps.
        """
        jumps: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == 1:
                    # Check all four diagonal directions
                    for dr, dc in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                        start = (row, col)
                        end = (row + dr, col + dc)
                        if self.is_valid_jump(start, end):
                            jumps.append((start, end))
        return jumps

    def play(self) -> None:
        """
        Simulate the game by performing jumps until no more jumps are possible.
        Rules:
        - Repeatedly find and perform valid jumps.
        - Stop when no more jumps are possible.
        """
        while True:
            jumps = self.find_possible_jumps()
            if not jumps:
                break  # No more jumps possible

            # Perform the first valid jump (can be optimized further)
            start, end = jumps[0]
            self.perform_jump(start, end)

        print(f"Total checkers removed: {self.removed_checkers}")

    def display_board(self) -> None:
        """
        Display the current state of the board.
        Rules:
        - Print the board with '•' for checkers and '.' for empty squares.
        """
        for row in self.board:
            print(" ".join("•" if cell == 1 else "." for cell in row))
        print()


# Main program
if __name__ == "__main__":
    print("Initial Board:")
    # Initialize the board with empty squares
    initial_board = [[0 for _ in range(8)] for _ in range(8)]
    game = Checkerboard(board=initial_board)
    game.display_board()

    print("Playing the game...")
    game.play()

    print("Final Board:")
    game.display_board()