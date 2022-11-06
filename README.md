Author: Claire Grady 

Version: 1.0

Program: Uses a form of Depth-First Search to solve a simple sudoku puzzle

Algorithm: The algorithm is a form of Depth-First Search and is also known as a backtracking 
algorithm due to its recursive nature. It starts by checking to see if the sudoku grid has 
any zeros (all blank cells were replaced with zeros). If it does not, then the puzzle is 
solved and the GUI is displayed and CLI printed out. If it does, it then iterates through
the possible values (1-9), checks to see if that value is in the current row, column or 3x3 
grid and if it is NOT it then replaces the zero with that value. It then calls itself and 
repeats the process detailed above. If it at some point there are zeros remaining but there 
are no values that pass the checking functions an error has occurred. The algorithm then 
reassigns 0 to that cell and tests out the next value in the range of one through nine. 
This process gets repeated until there are no zeros remaining in the puzzle. 

Compiling Instructions:
python3 cgrady3.py

OPTIONAL:
If you would like to try out the hardest sudoku ever created then compile with...
python3 cgrady3.py --level hard

usage: cgrady3.py [-h] [--level LEVEL]

Option to Change Sudoku Level

optional arguments:
  -h, --help     show this help message and exit
  --level LEVEL  easy or hard

Default Level: easy
