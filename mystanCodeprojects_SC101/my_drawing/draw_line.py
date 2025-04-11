"""
File: draw_line.py
Name:Sandy
-------------------------
TODO:
The position of an odd-numbered click serves as the starting point of the line.
At this moment, a hollow circle with a fixed radius of SIZE is drawn, centered at the mouse click position.
The position of an even-numbered click serves as the ending point of the line.
At this moment, the hollow circle disappears, and a straight line is drawn
from the previous click to the current click position.

Please note that the entire process only involves clicking on the window—no dragging actions are required.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
window = GWindow()
has_added = False  # use a switch to know the click is odd or even
hole = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global has_added, hole

    if not has_added:  # odd times
        hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        hole.filled = False
        window.add(hole)
        has_added = True
    else:
        if hole is not None:
            window.remove(hole)  # remove first hole and add the line
            line = GLine(hole.x + SIZE / 2, hole.y + SIZE / 2, mouse.x, mouse.y)
            window.add(line)
        has_added = False  # even times


if __name__ == "__main__":
    main()
