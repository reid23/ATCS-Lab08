'''
Isaac and Reid
This file contains the backend for minesweeper. It is a board class which does all the computations and stores the game's state.

Written entirely by Reid
'''

import numpy as np
from scipy.signal import convolve # if this doesn't work, do `~$ pip install scipy` or similar depending on your pip/python setup
class Board:
    def __init__(self):
        """Creates a new Board object.
        """
        self.mines = np.array([1]*10 + [0]*54) # start with flat array of 1s and 0s representing mines
        np.random.shuffle(self.mines) # shuffle it for random mine locations
        self.mines = self.mines.reshape((8,8)) # turn it into a non-flat array (8x8 bc that's our board size)
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
        if self.mines[row, col]==1: return False # if square clicked is a mine, the player has lost
        self._BFS(row, col) # otherwise, do the whole reveal thing, showing all the squares
        if sum(sum(self.visible)) == 54: return True # if all non-mines are visible, the player has won
        return self.getBoard() # then return the board in case it's useful.
    def getBoard(self):
        """returns a 8x8 array describing the current board state. Squares' values are the number on them. If the value is -1, the square is not visible yet.

        Returns:
            np.ndarray: 8x8 array describing the current board state. -1 means not visible, everything else is just the number the player sees.
        """
        return (self.clues+1)*self.visible - 1
    def _DFS(self, row, col):
        """recursive Depth-First Search implementation to show clues
        yes, it's supposed to be BFS, oops. I'll change it, but this works fine for testing.

        Args:
            row (int): the row of the move, with 0 as top and 7 as bottom
            col (int): the column of the move, with 0 as left and 7 as right
        """
        self.visible[row, col] = 1 # set this node to visible
        if self.clues[row, col]>0: return # check if any neighbors have mines, return if they do, since we can't continue searching here
        neighbors = np.array([ # get all neighbors
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
                self.visible[i[0], i[1]]=1 # set it to visible, and recurse to search further
                self._DFS(*i)
            elif self.visible[i[0], i[1]]==0: # if it does have adjacent mines, just set it to visible and don't recurse further.
                self.visible[i[0], i[1]]=1
    @staticmethod
    def neighbors(row, col):
        """gets the coordinates of the neighbors of row, col. Returns tuples for hashability.

        Args:
            row (int): the row of the square whose neighbors you want to find
            col (int): the column of the square whose neighbors you want to find

        Returns:
            tuple[tuple[int]]: a tuple of 2-tuples describing the coordinates. 
        """
        return (
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1),
            (row, col+1),
            (row, col-1),
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
        )

    def _BFS(self, row, col):
        """uses breadth-first search to reveal all squares from a player's move

        Args:
            row (int): the row of the move
            col (int): the column of the move
        """
        q = [(row, col)] # this will be our queue for the black box. Initialize it with the starting square.
        visited = set() # empty set to keep track of where we've gone
        while len(q)>0: # while we still have things to look at:
            cur = q.pop(0) # get the first square from he queue
            self.visible[cur[0], cur[1]] = 1 # make it visible
            if self.clues[cur[0], cur[1]] > 0: # if it has adjacent mines, stop revealing squares
                continue
            for cell in Board.neighbors(*cur):# otherwise add all the neighbors to the queue to investigate next
                # if the square has already been looked at or is out of bounds, skip it
                if cell in visited or not (0<=cell[0]<=7 and 0<=cell[1]<=7):
                    continue
                # otherwise note that the cell has been visited and add it to the black box to investigate later
                visited.add(cell)
                q.append(cell)
            


# a text-based implementation of the game for testing
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

