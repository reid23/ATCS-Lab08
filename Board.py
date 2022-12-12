import numpy as np
from scipy.signal import convolve
class Board:
    def __init__(self):
        """Creates a new Board object.
        """
        self.mines = np.array([1]*10 + [0]*54) #start with flat array of 1s and 0s representing mines
        np.random.shuffle(self.mines) #shuffle it for random mine locations
        self.mines = self.mines.reshape((8,8)) #turn it into a non-flat array (8x8 bc that's our board size)
        self.clues = convolve(self.mines, np.array([[1,1,1],[1,0,1],[1,1,1]]), 'same') # convolution sums up all the neighbors, so each square in clues is the number of neighbors which are mines.
        self.visible = np.zeros((8, 8), dtype=int) # like a boolean mask. This dictates which squares are visible.
    def move(self, row, col):
        """enters a move at row, col of the grid.

        Args:
            row (int): the row (down from the top, starting at zero) which the player chose
            col (int): the column (from left, starting at zero)

        Returns:
            bool | np.array: either a bool or numpy array. Bool if the game is over, True if won, False if lost. Otherwise ndarray describing what should be drawn.
        """
        if self.mines[row, col]==1: return False #if square clicked is a mine, the player has lost
        self._DFS(row, col) #otherwise, do the whole reveal thing, showing all the squares
        if sum(sum(self.visible)) == 54: return True #if all non-mines are visible, the player has won
        return self.getBoard() #then return the board in case it's useful.
    def getBoard(self):
        """returns a 8x8 array describing the current board state. Squares' values are the number on them. If the value is -1, the square is not visible yet.

        Returns:
            np.ndarray: 8x8 array describing the current board state. -1 means not visible, everything else is just the number the player sees.
        """
        return (self.clues+1)*self.visible - 1
    def _DFS(self, row, col):
        """recursive Depth-First Search implementation to show clues
        yes, it's supposed to be BFS. I'll change it, but this works fine for testing.

        Args:
            row (int): the row of the move, with 0 as top and 7 as bottom
            col (int): the column of the move, with 0 as left and 7 as right
        """
        self.visible[row, col] = 1 #set this node to visible
        if self.clues[row, col]>0: return #check if any neighbors have mines, return if they do, since we can't continue searching here
        neighbors = np.array([ #get all neighbors
            [row+1, col-1],
            [row+1, col],
            [row+1, col+1],
            [row, col+1],
            [row, col-1],
            [row-1, col-1],
            [row-1, col],
            [row-1, col+1],
        ])
        for i in neighbors:
            if len(i[i<0]) + len(i[i>7]) != 0: continue # check if neighbor is in bounds
            if self.clues[i[0], i[1]]==0 and self.visible[i[0], i[1]]==0: # check if square has no adjacent mines andd is not yet visible
                self.visible[i[0], i[1]]=1 #set it to visible, and recurse to search further
                self._DFS(*i)
            elif self.visible[i[0], i[1]]==0: # if it does have adjacent mines, just set it to visible and don't recurse further.
                self.visible[i[0], i[1]]=1
        

if __name__=='__main__':
    b=Board()
    while True:
        print(b.getBoard())
        row, col = input('move: ').split(',')
        print(row, col)
        results = b.move(int(row), int(col))
        if isinstance(results, bool): break
    print('game over')
    print(b.mines)

