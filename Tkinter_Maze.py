from tkinter import *
from os import system
from random import randint
system("cls")

# Single cell drawing (at first i used create_rectangle directly in the code but its cleaner to have a separate function)
def draw_cell(row, column, color):
    x1 = column * cell_size
    x2 = x1 + cell_size
    y1 = row * cell_size
    y2 = y1 + cell_size
    maze.create_rectangle(x1, y1, x2, y2, fill = color)
    
# Create square maze filled with walls
cell_size = 15
maze_size = 50 # height = width
t = [ [0]*3 for i in range(3)]
# Apparently this is the best way to init a 2D array according to GfG
cell_map = [['wall' for row in range(maze_size)] for column in range(maze_size)] # rows x columns, all walls at the beginning

def maze_init():
    for row in range(maze_size):
        for column in range(maze_size):
            cell_map[row][column] = 'wall'
            draw_cell(row, column, 'black') # Walls are black, the path is white.

# Implementation of Prim's Algorithm
    # Pick random cell as starting point; make sure to start randomization at one, since 0 will be reserved for exits
starting_row = randint(1, maze_size)
starting_column = randint(1, maze_size)

cell_map[starting_row][starting_column] = 'path'
#draw_cell(starting_row, starting_column, 'white')


# Maze Window
window = Tk()
window.title("Maze") # Apparently could've also done window = Tk(className = 'Window Title')
window.geometry("750x750")  # maze_size * cell_size = 15 * 50 = 750

maze = Canvas(window, bg = 'grey', height = maze_size * cell_size, width = maze_size * maze_size)
maze.pack()

maze_init()
window.mainloop()