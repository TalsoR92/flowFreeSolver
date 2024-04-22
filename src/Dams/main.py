from Dams.include import *
from Dams.class_files.Board import *
import json


def create_response_json(board, num_level, width, height):
    """
    Create a JSON response for board num_level with n*n size.
    """
    # Create a list of lists containing the color of each cell in the board
    board_colors = [[cell.color for cell in row] for row in board.board]
    print(board_colors)
    
    # Define the file path
    file_path = f"levels_res_on_json/board_res_{width}-{height}.json"

    # Load existing JSON data from file, if any
    try:
        with open(file_path, "r") as file:
            levels_data = json.load(file)
    except FileNotFoundError:
        levels_data = {}

    # Add or update the data for the current level
    levels_data[f"level_{num_level}"] = board_colors

    # Write the updated JSON data back to the file
    with open(file_path, "w") as file:
        json.dump(levels_data, file, indent=4)
    
def sum_list(all_paths):
    """
    Sum the lengths of all the lists in a list of lists.
    """
    # Initialiser la somme à zéro
    total_paths = 0

    # Parcourir chaque liste dans all_paths
    for path_list in all_paths:
        # Ajouter la longueur de la liste à la somme totale
        total_paths += len(path_list)
    return total_paths

def main(flow_matrix, size_board, num_level):
    # Création d'une instance de Board
    board = Board(width=size_board, height=size_board)

    # Appel de la méthode create_class_board avec la flow_matrix donnée
    # print(flow_matrix)
    board.create_class_board_with_Case(flow_matrix)

    # print(board)

    opti = Opti(CheckReachable.NEAR_3_THINGS)
    print("opti.check_reachable:", opti.check_reachable, "\n")
    all_paths = create_all_paths(board, opti)
    print("nb_paths:", sum_list(all_paths), "\n")

    find_and_apply_valid_combinations(board, all_paths, opti)
    # print(board)
    # create_response_json(board, num_level, size_board, size_board)