import numpy as np
from scipy.signal import convolve
class Board:
    def __init__(self):
        self.mines = np.array([1]*10 + [0]*54)
        np.random.shuffle(self.mines)
        self.mines = self.mines.reshape((8,8))
        self.clues = convolve(self.mines, np.array([[1,1,1],[1,0,1],[1,1,1]]), 'same')
        self.visible = np.zeros((8, 8))
    def getBoard(self):
        return self.clues*self.visible
    def getMoveResults(self, row, col):
        if self.mines[row, col]==1: return True
        self._BFS(row, col)
        return self.getBoard()
    def _BFS(self, row, col):
        self.visible[row, col] = 1
        if self.clues[row, col]>0: return
        neighbors = np.array([
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
            if len(i[i<0]) + len(i[i>7]) != 0: continue
            if self.clues[i[0], i[1]]==0 and self.visible[i[0], i[1]]==0:
                self.visible[i[0], i[1]]=1
                self._BFS(*i)
            elif self.visible[i[0], i[1]]==0:
                self.visible[i[0], i[1]]=1
        

if __name__=='__main__':
    b=Board()
    while True:
        print(b.getBoard())
        row, col = input('move: ').split(',')
        print(row, col)
        results = b.getMoveResults(int(row), int(col))
        if isinstance(results, bool): break
    print('game over')
    print(b.mines)

