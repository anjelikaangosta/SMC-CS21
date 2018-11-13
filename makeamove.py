from graphics import *

def create_window():
    win = GraphWIn()
    win.setCoords (-6, -6, 6, 6)
    win.setBackground ("green")
    p = Point (0,0)
    p.draw(win)
