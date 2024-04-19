from Dams.include import *
from Dams.class_files.Board import *

def main(flow_matrix, size_board):
    # Création d'une instance de Board
    board = Board(width=size_board, height=size_board)

    # Appel de la méthode create_class_board avec la flow_matrix donnée
    print(flow_matrix)
    board.create_class_board_with_Case(flow_matrix)

    print(board)
    create_all_paths(board)
    print(board)