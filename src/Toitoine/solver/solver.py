from Toitoine.board.board import *
from Toitoine.solver.creation_path import *
from Toitoine.solver.extend_path import *

def solver(board):
    extends_path(board)
    while board.points != []:
        create_all_path(board)
        extends_path(board)
