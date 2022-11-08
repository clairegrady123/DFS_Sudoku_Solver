import numpy as np
import time
import tkinter
from tkinter import *
import argparse

#check if potential value is in current row
def current_row(completed_grid, index, val):
    if (val in completed_grid[index[0],:]):
        return True
    return False

#check if potential value is in current column
def current_col(completed_grid, index, val):
    if (val in completed_grid[:,index[1]]):
        return True
    return False

#check if potential value is in current 3x3 grid
def current_sub_array(completed_grid, index, val):
    for i in range((index[0]-index[0]%3), (index[0]-index[0]%3)+3):
        for j in range((index[1]-index[1]%3), (index[1]-index[1]%3)+3):
            if (val == completed_grid[i][j]):
                return True
    return False

#call all checking functions
def check(completed_grid, val, index):
    if (not current_row(completed_grid, index, val) and not current_sub_array(completed_grid, index, val)\
        and not current_col(completed_grid, index, val)):
        return True
    else:
        return False

#check for remaining zeros
def find_zeros(grid, zero_indices):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                zero_indices[0] = i
                zero_indices[1] = j
                return True
    return False

#recursive backtracking algorithm
def sudoku_backtracking(completed_grid):
    zero_indices = [0,0]
    #stopping condition
    if (not find_zeros(completed_grid, zero_indices)):
        return True
    i = zero_indices
    for val in range(1, 10):
        if (check(completed_grid, val, i)):
            completed_grid[i[0],i[1]] = val
            if (sudoku_backtracking(completed_grid)):
                return True
            completed_grid[i[0], i[1]] = 0
    return False

#create horizontal lines on gui
def horizontal(k,l,j, canvas, colour, width):
    canvas.create_line(k, j, l, j, width=width, fill=colour)

#create vertical lines on gui
def vertical(i,l,j,canvas, colour, width):
    canvas.create_line(l, i, l, j, width=width, fill=colour)

#replicate the sudoku grid on the gui
def create_grid(canvas):
     i = 10
     j = 74
     k = 10
     l = 74
     start = 10
     dim = 64
     for n in range(9):
         for m in range(9):
             if m != 2 and m != 5 and m != 8:
                 vertical(i, l, j, canvas, "grey80", 2)
             if n != 2 and n != 5 and n != 8:
                horizontal(k, l, j, canvas, "grey80", 2)
             if n == 8 and m == 7:
                 vertical(start, dim*3+start, j, canvas, "Black", 3)
                 vertical(start, dim*6+start, j, canvas, "Black", 3)
                 horizontal(start, j, dim*3+start, canvas, "Black", 3)
                 horizontal(start, j, dim*6+start, canvas, "Black", 3)
             l += 64
             k += 64
         i+=64
         j+=64
         l=74
         k=10


#define gui
def gui(grid_to_display, grid):
    root = Tk()
    root.title("Sudoku")
    root.configure(background="white")
    canvas = Canvas(root, width=9.25 * 64, height=9.25 * 64, bg="white")
    canvas.create_rectangle(10, 10, 586, 586, fill="white", outline="black", width=3)
    create_grid(canvas)
    number_positions = []
    start_position = 42
    count = 0
    for i in range(9):
        for j in range(9):
            number_positions.append([start_position + (j * 64), start_position + (i * 64), grid_to_display[i][j]])
            canvas.create_text(number_positions[count][0], number_positions[count][1],
                               text=number_positions[count][2], font="Helvetica 24 bold", fill="Black")
            count += 1
    canvas.pack()
    #canvas2 = Canvas(root, width=9.25 * 64, height=20, bg="white")
    #canvas2.pack()
    def exit_program():
        root.destroy()
    number_positions = []
    start_position = 42
    #display numbers in the grid
    def display_program(canvas, grid_to_display):
        count = 0
        for i in range(9):
            for j in range(9):
                number_positions.append([start_position + (j * 64), start_position + (i * 64), grid[i][j]])
                canvas.create_text(number_positions[count][0], number_positions[count][1],
                                text=number_positions[count][2], font="Helvetica 24 bold", fill="Black")
                count += 1
    exit = Button(root, text="Exit", command=exit_program)
    exit.pack(side=tkinter.RIGHT)
    display = Button(root, text="Completed Sudoku", command=lambda: display_program(canvas, grid))
    display.pack(side=tkinter.RIGHT)
    root.mainloop()


#main function that drives the program
def main():
    start_time = time.time()
    display_easy_grid = np.array([[9, None, None, 1, 7, None, 4, None, 2], [1, 6, None, None, 4, None, None, 9, 5], 
                    [None, None, 8, None, None, 3, None, None, None], [None, 1, None, 9, None, None, 5, 7, 3],
                    [None, 4, None, None, None, None, None, 2, None], [5, 8, 9, None, None, 7, None, 1, None], 
                    [None, None, None, 4, None, None, 7, None, None], [6, 7, None, None, 2, None, None, 5, 8],
                    [3, None, 1, None, 5, 8, None, None, 6]])
    display_hardest_grid = np.array([[6, None, None, None, None, 8, 9, 4, None], [9, None, None, None, None, 6, 1, None, None], 
                    [None, 7, None, None, 4, None, None, None, None], [2, None, None, 6, 1, None, None, None, None],
                    [None, None, None, None, None, None, 2, None, None], [None, 8, 9, None, None, 2, None, None, None], 
                    [None, None, None, None, 6, None, None, None, 5], [None, None, None, None, None, None, None, 3, None],
                    [8, None, None, None, None, 1, 6, None, None]])
    easy_grid = np.array([[9,0,0,1,7,0,4,0,2],[1,6,0,0,4,0,0,9,5],[0,0,8,0,0,3,0,0,0],[0,1,0,9,0,0,5,7,3],
                               [0,4,0,0,0,0,0,2,0],[5,8,9,0,0,7,0,1,0],[0,0,0,4,0,0,7,0,0],[6,7,0,0,2,0,0,5,8],[3,0,1,0,5,8,0,0,6]])
    ## hardest ever apparently
    hardest_grid = np.array([[6, 0, 0, 0, 0, 8, 9, 4, 0], [9, 0, 0, 0, 0, 6, 1, 0, 0], [0, 7, 0, 0, 4, 0, 0, 0, 0],
                     [2, 0, 0, 6, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 8, 9, 0, 0, 2, 0, 0, 0], 
                     [0, 0, 0, 0, 6, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0, 3, 0], [8, 0, 0, 0, 0, 1, 6, 0, 0]])
    f = open("command_line.txt", "r")
    print(f.read())
    
    level = "easy"
    parser = argparse.ArgumentParser(exit_on_error=False, description='Option to Change Sudoku Level')
    parser.add_argument('--level', type=ascii, required=False, default=level, help = 'String value for level: easy or hard')
    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        print("You must choose an option --level or --help!\]n")

    level = args.level.replace("'","")
    if level == "hard":
        grid = hardest_grid
        display_grid = display_hardest_grid
        text = "Searching started...this puzzle will take around 90 seconds to solve\n"
    else:
        grid = easy_grid
        display_grid = display_easy_grid
        text = "Searching started...\n"
    print(text)

    if (sudoku_backtracking(grid)):
        end_time = time.time()
        print("Searching complete!\n")
        print("Total elapsed time was", round(((end_time - start_time) * 1000), 2), "milliseconds!\n")
        print("Completed Sudoku Puzzle\n")
        print(grid, "\n")
        gui(display_grid, grid)
    else:
        print("There is no solution to this sudoku")


if __name__ == "__main__":
    main()
