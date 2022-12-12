'''
Contains GUI for minesweeper.
Done entirely by Isaac.
'''

from graphics import *
from Board import Board
from Button import Button
from BoardCell import BoardCell
import time

def main():
    # Creates graphics window and replay and quit buttons
    win = GraphWin("Minesweeper", 400, 400)
    replayButton = Button(100, 200, 100, 100, "Replay", win)
    quitButton = Button(300, 200, 100, 100, "Quit", win)
    done = False
    gameOver = False
    # While the user hasn't quit (done)
    while done == False:
        gameOver = False
        # Creates new board, an array that will store the result of board, and a 2d array for storing the Board Cells
        backboard = Board()
        board = []
        boardCells = []
        # Fills up the 2d array with empty Board Cells and draws them
        for i in range(8):
            boardCells.append([])
        for i in range(8):
            for j in range(8):
                boardCells[i].append(BoardCell(Point(i*50, j*50), Point((i+1)*50-1, (j+1)*50-1), "gray", Point(i*50+25, j*50+25), "", "black", 20))
        for i in range(8):
            for j in range(8):
                boardCells[i][j].draw(win)
        # While the game isn't over
        while gameOver == False:
            # Wait for a click and convert the point of the click to an index corresponding to board and BoardCells
            clickPoint = win.getMouse()
            clickX = int(clickPoint.getX()//50)
            clickY = int(clickPoint.getY()//50)
            # Update board by performing the move
            # Sets a variable result to what the move returns if it's True or False
            result = backboard.move(clickX, clickY)
            # Sets another variable to what "getBoard" returns if a normal move was executed
            board = backboard.getBoard()
            # Player wins
            if result is True:
            # Clear the board
                for i in range(8):
                    for j in range(8):
                        boardCells[i][j].undraw()
                # Display win message along with the two buttons
                endMessage = Text(Point(200, 100), "You Win")
                endMessage.setTextColor("black")
                endMessage.setSize(20)
                endMessage.draw(win)
                replayButton.activate()
                replayButton.draw()
                quitButton.activate()
                quitButton.draw()
                clicked = False
                # While the user hasn't clicked a button
                while clicked == False:
                    buttonClick = win.getMouse()
                    # If replay, break out of this loop and acknowledge the game as over
                    if replayButton.clicked(buttonClick):
                        clicked = True
                        gameOver = True
                    # If quit, break out of this loop and acknowledge both the game and the overall interface as over
                    elif quitButton.clicked(buttonClick):
                        clicked = True
                        gameOver = True
                        done = True
                # Undraw message and buttons
                endMessage.undraw()
                replayButton.deactivate()
                replayButton.undraw()
                quitButton.deactivate()
                quitButton.undraw()
            # Player loses
            elif result is False:
                # Update the clicked cell to indicate a mine
                boardCells[clickX][clickY].undraw()
                boardCells[clickX][clickY].setRectFill("white")
                boardCells[clickX][clickY].setTextMessage("M")
                boardCells[clickX][clickY].draw(win)
                # Wait two seconds so the player can see the mine
                time.sleep(2)
                # Below code is exact same as win case, but the message is a losing one
                for i in range(8):
                    for j in range(8):
                        boardCells[i][j].undraw()
                endMessage = Text(Point(200, 100), "You Lose")
                endMessage.setTextColor("black")
                endMessage.setSize(20)
                endMessage.draw(win)
                replayButton.activate()
                replayButton.draw()
                quitButton.activate()
                quitButton.draw()
                clicked = False
                while clicked == False:
                    buttonClick = win.getMouse()
                    if replayButton.clicked(buttonClick):
                        clicked = True
                        gameOver = True
                    elif quitButton.clicked(buttonClick):
                        clicked = True
                        gameOver = True
                        done = True
                endMessage.undraw()
                replayButton.deactivate()
                replayButton.undraw()
                quitButton.deactivate()
                quitButton.undraw()
            # All other moves
            else:
                # Loops through all cells
                for i in range(8):
                    for j in range(8):
                        # Undraw the cell
                        boardCells[i][j].undraw()
                        # If the cell hasn't been clicked, set it to gray
                        if board[i][j] == -1:
                            boardCells[i][j].setRectFill("gray")
                        # Else, it's been clicked, so make it white
                        else:
                            boardCells[i][j].setRectFill("white")
                        # If the cell has bombs as neighbors, display the number of bombs
                        if board[i][j] > 0:
                            boardCells[i][j].setTextMessage(str(board[i][j]))
                        # Draw the edited cell
                        boardCells[i][j].draw(win)
    # Graphics window closes with one last mouse click
    win.getMouse()
    win.close()

main()
