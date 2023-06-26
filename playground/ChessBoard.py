import numpy as np
import matplotlib.pyplot as plt

class ChessBoard:
  def __init__(self):
    self.grid = np.ones((8, 8, 3))
    for row in range(8):
      for col in range(8):
        if (row + col) % 2 == 0:
          self.grid[row][col] = (1, 1, 1)
        else:
          self.grid[row][col] = (0, 0, 0)

  def add_red(self, row, col):
    self.grid[row][col] = (1, 0.2, 0)

  def add_blue(self, row, col):
    self.grid[row][col] = (0, 1, 1)

  def render(self):
    plt.imshow(self.grid)

  def is_under_attack(self):
    red_row, red_col = None, None#find red
    blue_row, blue_col = None, None#find blue

    for i in range(8): #find red and blue
      for j in range(8): #find red and blue
        
        if np.array_equal(self.grid[i][j], np.array([1, 0.2, 0])): #find red
          red_row, red_col = i, j #find red
        elif np.array_equal(self.grid[i][j], np.array([0, 1, 1])): #find blue
          blue_row, blue_col = i, j #find blue

    if red_row is None or blue_row is None: #if red or blue is not found return false
      return False

    if red_row == blue_row or red_col == blue_col: #if red or blue is in the same row or column return true
      return True

    if abs(red_row - blue_row) == abs(red_col - blue_col): #if red or blue is in the same diagonal return true
      return True
    #q: what is abs doing
    #a: abs is returning the absolute value of the difference between the red and blue row and column
    return False

board = ChessBoard()
board.add_blue(3, 3)
board.add_red(3, 4)
board.render()
print('Red under attack?', board.is_under_attack())
