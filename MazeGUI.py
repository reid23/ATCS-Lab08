import graphics as g
from Button import Button

win = g.GraphWin("MazeLauncher")

instructions = g.Text(g.Point(150, 80), "To begin, enter the dimensions of the maze you want to generate.\nThe total area must be less than 1000, and each value must be at least 1.")
width = g.Entry(g.Point(100, 100), 10)
width.setText("width")
height = g.Entry(g.Point(200, 100), 10)
height.setText("height")
generate = Button(150, 150, 50, 15, "generate maze")

instructions.draw(win)
width.draw(win)
height.draw(win)
generate.draw(win)

while True:
    if generate.clicked(win.getMouse()):
        try:
            w, h = int(width.getText()), int(height.getText())
        except ValueError:
            # give error message
            continue
        if w*h>1000: 
            # give error message
            continue
        if w<1 and h<1: 
            # give error message
            continue
        break
win.close()
g = makeMazeArray()
win = g.GraphWin("Maze")







