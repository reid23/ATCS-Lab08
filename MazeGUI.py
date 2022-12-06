import graphics as g
from Button import Button
from Lab08Maze import makeMazeArray
import numpy as np
import matplotlib.pyplot as plt
from sys import setrecursionlimit

def main():
    win = g.GraphWin("MazeLauncher", 300, 250)

    instructions = g.Text(g.Point(150, 50), "Enter the dimensions of the maze you want to generate.\n\nThe total area must be at most 1000, and\neach value must be at least 1.")
    
    area_override = False
    override_button = Button(150, 100, 150, 20, "Override max area limitation", win)
    
    height = g.Entry(g.Point(100, 160), 10)
    height_label = g.Text(g.Point(200, 140), "Rows:")
    width = g.Entry(g.Point(200, 160), 10)
    width_label = g.Text(g.Point(100, 140), "Columns:")

    generate = Button(100, 210, 80, 20, "generate maze", win)
    quit_button = Button(200, 210, 80, 20, "quit", win)


    instructions.draw(win)
    width.draw(win)
    width_label.draw(win)
    height.draw(win)
    height_label.draw(win)
    generate.draw(win)
    quit_button.draw(win)
    override_button.draw(win)
    while True:
        generate.activate()
        quit_button.activate()
        override_button.activate()
        while True:
            click = win.getMouse()
            if quit_button.clicked(click): exit()
            if override_button.clicked(click):
                area_override = "Override" in override_button.getLabel()
                override_button.setLabel("Re-enable max area limitation" if area_override else "Override max area limitation")
                if area_override:
                    override_button.setLabel("Re-enable max area limitation")
                    instructions.setText("Enter the dimensions of the maze you want to generate.\n\nEach value must be at least 1.")
                else:
                    override_button.setLabel("Override max area limitation")
                    instructions.setText("Enter the dimensions of the maze you want to generate.\n\nThe total area must be at most 1000, and\neach value must be at least 1.")
            if generate.clicked(click):
                try:
                    w, h = int(width.getText()), int(height.getText())
                except ValueError:
                    instructions.setText("Error: invalid dimensions.\nPlease enter integers greater than 1\nwhich multiply to at most 1000.")
                    continue
                if w*h>1000 and not area_override: 
                    instructions.setText("Error: Maze too large.\nPlease enter dimensions \nwhich multiply to at most 1000.")
                    continue
                if w<1 or h<1: 
                    instructions.setText("Error: Maze too small.\nPlease enter dimensions of at least 1.")
                    continue
                break
        if area_override: instructions.setText("Enter the dimensions of the maze you want to generate.\n\nEach value must be at least 1.")
        else: instructions.setText("Enter the dimensions of the maze you want to generate.\n\nThe total area must be at most 1000, and\neach value must be at least 1.")
        if area_override: setrecursionlimit(w*h)
        maze = np.array(makeMazeArray(h, w))
        maze = np.concatenate((maze[:, :, np.newaxis], maze[:, :, np.newaxis], maze[:, :, np.newaxis]), axis=2)

        maze[maze!=3]=255
        maze[maze==3]=0

        maze[1,0] = np.array([0,255,0])
        maze[-2, -1] = np.array([255,0,0])
        plt.close()
        plt.imshow(maze)
        plt.title(f'{h}x{w} maze generated successfully. Start is green and end is red.')
        plt.axis('off')
        plt.show(block=False)

if __name__=='__main__':
    main()






