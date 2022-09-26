import curses

from curses import wrapper
import queue
import time

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j, value)
                
def main(stdscr):
    curses.init_pair(1, curses.COLOUR_BLUE, curses.COLOUR_CLACK)
    curses.init_pair(1, curses.COLOUR_RED, curses.COLOUR_CLACK)
    #blue_and_black = curses.colour_pair(1)
    
    stdscr.clear()
    print_mazent(maze, stdscr)
#   stdscr.addstr(0,0, "Hello World!", blue_and_black)
    stdscr.refresh()
    stdscr.getch()
    
wrapper(main)