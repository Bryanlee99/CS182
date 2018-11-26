from sudoku import *
sudoku = Sudoku(boardEasy)
for a in sudoku.board:
    print a
print ""
sudoku._initLocalSearch()
sudoku.randomRestart()
for a in sudoku.board:
    print a
sudoku.gradientDescent((1,0), (1,4))