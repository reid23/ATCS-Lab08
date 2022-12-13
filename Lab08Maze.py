'''
Isaac and Reid
This file contains the GUI for the Maze problem.

It was written entirely by Reid.
'''

import graphics as g # graphics library
from Button import Button # button class from last year
from MazeBackend import makeMazeArray # Isaac's code
import numpy as np
import matplotlib.pyplot as plt # for showing maze
from sys import setrecursionlimit # for overriding limits

def main():
    win = g.GraphWin("MazeLauncher", 300, 250) # maze builder window

    # next bit creates all the graphics objects for the window and draws them
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

    # main game loop
    while True:
        # activate all the buttons
        generate.activate()
        quit_button.activate()
        override_button.activate()

        # loop to handle all button clicks
        while True:
            click = win.getMouse() # get click
            if quit_button.clicked(click): exit() #check quit button
            if override_button.clicked(click): # check override button

                #handle override button: swap labels/instructions, and set area_override
                area_override = "Override" in override_button.getLabel()
                override_button.setLabel("Re-enable max area limitation" if area_override else "Override max area limitation")
                if area_override:
                    override_button.setLabel("Re-enable max area limitation")
                    instructions.setText("Enter the dimensions of the maze you want to generate.\n\nEach value must be at least 1.")
                else:
                    override_button.setLabel("Override max area limitation")
                    instructions.setText("Enter the dimensions of the maze you want to generate.\n\nThe total area must be at most 1000, and\neach value must be at least 1.")
            
            # check generate button
            if generate.clicked(click):
                #handle maze generation

                #get input from boxes and make sure it is valid input
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

                # if it's valid, break out of the button handler loop to generate and display the maze
                break
        # reset instruction text. This is in case the last text displayed was an error.
        # Check area_override before setting text to make sure we set the correct instructions
        if area_override: instructions.setText("Enter the dimensions of the maze you want to generate.\n\nEach value must be at least 1.")
        else: instructions.setText("Enter the dimensions of the maze you want to generate.\n\nThe total area must be at most 1000, and\neach value must be at least 1.")
        
        # this is what the area_override actually does
        # must be set to w*h because that's the theoretical max recursion depth of DFS
        if area_override: setrecursionlimit(w*h)

        #generate the maze
        maze = np.array(makeMazeArray(h, w))

        #turn the maze from shape (h,w) to (h,w,3) (just copy it 3 times along the last axis, so we get an (h, w) array of [1,1,1] or something)
        maze = np.concatenate((maze[:, :, np.newaxis], maze[:, :, np.newaxis], maze[:, :, np.newaxis]), axis=2)

        #convert rgb to 8-bit values
        maze[maze!=3]=255 # if it's not a wall (3), set it to [255,255,255], which is white.
        maze[maze==3]=0   # if it's a wall, set it to [0,0,0], which is black.

        maze[1,0] = np.array([0,255,0]) # set the start to green
        maze[-2, -1] = np.array([255,0,0]) # set the end to red

        # show the maze with matplotlib
        plt.close() #flush last maze
        plt.imshow(maze) # show it
        plt.title(f'{h}x{w} maze generated successfully. Start is green and end is red.') # add title
        plt.axis('off') # to make it prettier, turn of axes
        plt.show(block=False) #block=False allow the program to continue running so we can generate another maze while this one is displayedd

if __name__=='__main__':
    main()






