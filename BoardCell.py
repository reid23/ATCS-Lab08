from graphics import *

# Class for cells in minesweeper
class BoardCell():
    # Constructor takes in parameters for opposite points of the rectangle in the cell, the color of the rectangle,
    # and the center point, message, color, and size of the text
    def __init__(self, RectPoint1, RectPoint2, RectFill, TextPoint, TextMessage, TextColor, TextSize):
        # Creates instance variables for the rectangle and text based on parameters
        self.rect = Rectangle(RectPoint1, RectPoint2)
        self.rect.setFill(RectFill)
        self.text = Text(TextPoint, TextMessage)
        self.text.setTextColor(TextColor)
        self.text.setSize(TextSize)
    # Draws the cell in the window
    def draw(self, window):
        self.rect.draw(window)
        self.text.draw(window)
    # Undraws the cell
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
    # Sets the fill of the rectangle
    def setRectFill(self, newFill):
        self.rect.setFill(newFill)
    # Sets the message of the text
    def setTextMessage(self, newMessage):
        self.text.setText(newMessage)