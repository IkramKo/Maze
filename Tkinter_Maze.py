from tkinter import *
from os import system
from random import randint
system("cls")


"""
    1. Init all cells to walls
    2. Implement Prim's algo to generate navigable cells
    3. Draw maze

    Drawing should be the last step; if I draw the entire maze in black (walls) from the start, i cant draw over those cells with white
    and to modify the color of an existing canvas object, i need its id/var name. Simpler to create the maze in the cell_map first and 
    draw last.
"""
"""
# Init maze with walls
cell_size = 15
maze_size = 50 # height = width

# Apparently this is the best way to init a 2D array according to GfG
cell_map = [['wall' for row in range(maze_size)] for column in range(maze_size)] # rows x columns, all walls at the beginning
    

"""
#            N3
#    N4  CURR_CELL   N2
#            N1
"""
# Verify and add neighboring wall cells that arent on the edge
def check_neighbors(row, column, neighbors):
    if row == 1 and column == 1:
        # Append([0, 1]) adds [0, 1] as a row, Extend([0, 1]) adds 0, 1 to the array (stays 1D)
        if cell_map[row + 1, column] == 'wall'
            neighbors.append([row + 1, column]) # N1
        neighbors.append([row, column + 1]) # N2
    elif row == 1 and column != 1:
        neighbors.append([row + 1, column]) # N1
        neighbors.append([row, column + 1]) # N2
        neighbors.append([row, column - 1]) # N4
    elif row != 1 and column == 1:
        neighbors.append([row + 1, column]) # N1
        neighbors.append([row, column + 1]) # N2
        neighbors.append([row - 1, column]) # N3
    elif row != 1 and column != 1:
        neighbors.append([row + 1, column]) # N1
        neighbors.append([row, column + 1]) # N2
        neighbors.append([row - 1, column]) # N3
        neighbors.append([row, column - 1]) # N4

# Implementation of Prim's Algorithm
    # Pick random cell as starting point; make sure to start randomization at one, since 0 will be reserved for exits
starting_row = randint(1, maze_size)
starting_column = randint(1, maze_size)
cell_map[starting_row][starting_column] = 'path'



# Single cell drawing (at first i used create_rectangle directly in the code but its cleaner to have a separate function)
def draw_cell(row, column, color):
    x1 = column * cell_size
    x2 = x1 + cell_size
    y1 = row * cell_size
    y2 = y1 + cell_size
    maze.create_rectangle(x1, y1, x2, y2, fill = color)

def draw_maze():
    for row in range(maze_size):
        for column in range(maze_size):
            if cell_map[row][column] == 'wall':
                draw_cell(row, column, 'black')
            elif cell_map[row][column] ==  'path':
                draw_cell(row, column, 'white')

#print(cell_map)
# Init array that will keep track of neighboring walls
neighbors = []
check_neighbors(starting_row, starting_column, neighbors)
while

print(neighbors)


# Maze Window
window = Tk()
window.title("Maze") # Apparently could've also done window = Tk(className = 'Window Title')
window.geometry("750x750")  # maze_size * cell_size = 15 * 50 = 750

maze = Canvas(window, bg = 'grey', height = maze_size * cell_size, width = maze_size * maze_size)
maze.pack()

draw_maze()
window.mainloop()
"""

walls = []
walls.append([0, 1])
walls.append([1, 1])
walls.append([2, 1])
walls.append([3, 1])
print(len(walls))
print(len(walls[0]))




"""
Hall of shame (deleted functions)

def maze_init():
    for row in range(maze_size):
        for column in range(maze_size):
            cell_map[row][column] = 'wall'
            draw_cell(row, column, 'black') # Walls are black, the path is white.
"""