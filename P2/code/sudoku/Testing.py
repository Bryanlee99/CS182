from sudoku import *
sudoku = Sudoku(boardHard)
sudoku.board

print sudoku.box(0)

print sudoku.col(0)

print sudoku.updateFactor(BOX, 0)
sudoku = sudoku.setVariable(0, 0, 8)
print sudoku.row(0)
print sudoku.updateAllFactors()
print sudoku.updateVariableFactors((1, 2))
print sudoku.getSuccessors()
solveCSP(Sudoku(boardEasy))