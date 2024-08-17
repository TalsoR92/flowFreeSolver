from Toitoine.board.board import *
from Toitoine.solver.solver import  *

def main(flow_matrix, size_board):
    board = Board(flow_matrix, size_board)
    solver(board)
    return
