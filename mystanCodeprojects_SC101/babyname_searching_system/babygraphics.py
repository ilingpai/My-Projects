"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 為了在width這個範圍裡劃出years個數的線條，透過這段code return index數的座標
    # 全長:GRAPH_MARGIN_SIZE到CANVAS_HEIGHT-GRAPH_MARGIN_SIZE，總共有13年+13個間隔
    x_int = GRAPH_MARGIN_SIZE+year_index * ((width - 2*GRAPH_MARGIN_SIZE) // len(YEARS))  # 頭間隔+第幾年*全長/總年數
    return int(x_int)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    width = CANVAS_WIDTH
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(width, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # 畫出對應的排名線，並加上名字跟排名，y值為排名/1000*(GRAPH_MARGIN_SIZE~CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    rank_h = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK
    name_num = 0
    for name in lookup_names:
        x_list = []
        y_list = []
        name_num += 1
        for i in range(len(YEARS)):
            x_list.append(get_x_coordinate(CANVAS_WIDTH, i))
            color = COLORS[name_num % len(COLORS)-1]
            if str(YEARS[i]) in name_data[name]:
                rank = int(name_data[name][str(YEARS[i])])
                y_list.append(GRAPH_MARGIN_SIZE+int(rank)*rank_h)
                canvas.create_text(x_list[i] + TEXT_DX, y_list[i], text=f'{name}{rank}', anchor=tkinter.SW, fill=color)
            else:
                y_list.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
                canvas.create_text(x_list[i] + TEXT_DX, y_list[i], text=f'{name}*', anchor=tkinter.SW, fill=color)

            if i >= 1:
                canvas.create_line(x_list[i-1], y_list[i-1], x_list[i], y_list[i], width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
