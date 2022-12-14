'''
Isaac and Reid

This module was written entirely by Reid.
'''

from graphics import *

class Button(GraphicsObject):
    """ A button is a labeled rectangle in a window .
    It is activated or deactivated with the activate ()
    and deactivate () methods . The clicked (p) method
    returns true if the button is active and p is inside it .
    """
    def __init__(self, xpos, ypos, width, height, label, win):
        """ Creates a rectangular button , eg:
        qb = Button (centerPoint , width , height , 'Quit')"""
        self.win=win
        center=Point(xpos, ypos)
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.label = Text(center, label)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)
    def setLabel(self, label: str):
        "sets the button's label to label"
        self.label.setText(label)
    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
    def setActive(self, active: bool):
        if active:
            self.activate()
        else:
            self.deactivate()
    def getActive(self):
        return self.active
    def getGraphicsObjects(self):
        return [self.label, self.rect]
    def draw(self, win=None):
        if win!=None: self.win=win
        self.rect.draw(self.win)
        self.label.draw(self.win)
    def undraw(self):
        self.label.undraw()
        self.rect.undraw()
    
    act=property(getActive, setActive)
    lab=property(getLabel, setLabel)