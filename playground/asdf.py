import numpy as np
import matplotlib.pyplot as plt

class ChessBoard:
    def __init__(self):
        # Create a grid of shape (8, 8, 3) with all elements set to 1 (white color)
        self.grid = np.ones((8, 8, 3))
        for row in range(8):
            for col in range(8):
                # Set the color of the grid cells based on the row and column index
                if (row + col) % 2 == 0:
                    self.grid[row][col] = (1, 1, 1)  # white
                else:
                    self.grid[row][col] = (0, 0, 0)  # black

    def add_red(self, row, col):
        # Set the color of the specified grid cell to red
        self.grid[row][col] = (1, 0.2, 0)

    def add_blue(self, row, col):
        # Set the color of the specified grid cell to blue
        self.grid[row][col] = (0, 1, 1)

    def render(self):
        # Display the grid as an image using matplotlib
        plt.imshow(self.grid)
        plt.axis('off')  # Remove axis ticks and labels
        plt.show()

    def is_under_attack(self):
        red_row, red_col = None, None
        blue_row, blue_col = None, None

        for i in range(8):
            for j in range(8):
                # Find the positions of the red and blue pieces in the grid
                if np.array_equal(self.grid[i][j], np.array([1, 0.2, 0])):
                    red_row, red_col = i, j
                elif np.array_equal(self.grid[i][j], np.array([0, 1, 1])):
                    blue_row, blue_col = i, j

        if red_row is None or blue_row is None:
            # If either red or blue piece is not present, return False
            return False

        # Check horizontal and vertical attacks
        if red_row == blue_row or red_col == blue_col:
            return True

        # Check diagonal attacks
        if abs(red_row - blue_row) == abs(red_col - blue_col):
            return True

        return False

board = ChessBoard()
board.render()  # Display the initial chessboard
board.add_blue(3, 3)  # Add a blue piece at position (3, 3)
board.add_red(3, 4)  # Add a red piece at position (3, 4)
board.render()  # Display the updated chessboard
print('Red under attack?', board.is_under_attack())  # Check if red is under attack
