from Dams.class_files.Board import *
from Dams.class_files.Opti import *
from Dams.printer.printer import *
from Dams.algo.opti_v1 import *
from Dams.algo.tools import *
from Dams.include import *
from typing import List, Any, Tuple, Deque, Dict, Optional
from copy import deepcopy


def neighboring_available_cases(board, pos, color):
    """
    Optimization:
        This function prohibits filling (PAS DE REMPLISSAGE).

    Determines the available neighboring cases around a given position on the game board for a specific color.

    Parameters:
        - pos: A Position object representing the current position on the game board.
        - color: A string representing the color to check for neighboring points.

    Returns:
        A tuple containing a boolean value and a list of positions:
            - If a neighboring point of the specified color is found adjacent to the given position,
              the function returns (True, [Position]), where Position represents the position of the found point.
            - If no neighboring point of the specified color is found adjacent to the given position,
              the function returns (False, [Position1, Position2, ...]), where Positions are instances of Position
              class representing the neighboring positions that are accessible from the given position.
    """
    neighbors = []

        # Vérification de la case à gauche
    if pos.x - 1 >= 0:
        curr_case = board.board[pos.y][pos.x - 1]
        if not curr_case.color:
            if (pos.x - 2 < 0 or board.board[pos.y][pos.x - 2].color != color or board.board[pos.y][pos.x - 2].is_free_point()) \
                    and (pos.y - 1 < 0 or board.board[pos.y - 1][pos.x - 1].color != color or board.board[pos.y - 1][pos.x - 1].is_free_point()) \
                    and (pos.y + 1 >= board.height or board.board[pos.y + 1][pos.x - 1].color != color or board.board[pos.y + 1][pos.x - 1].is_free_point()):
                neighbors.append(Position(pos.x - 1, pos.y))
        elif curr_case.is_point and curr_case.color == color and not curr_case.is_connected:
            return (True, [Position(pos.x - 1, pos.y)])

    # Vérification de la case en haut
    if pos.y - 1 >= 0:
        curr_case = board.board[pos.y - 1][pos.x]
        if not curr_case.color:
            if (pos.x - 1 < 0 or board.board[pos.y - 1][pos.x - 1].color != color or board.board[pos.y - 1][pos.x - 1].is_free_point()) \
                    and (pos.x + 1 >= board.width or board.board[pos.y - 1][pos.x + 1].color != color or board.board[pos.y - 1][pos.x + 1].is_free_point()) \
                    and (pos.y - 2 < 0 or board.board[pos.y - 2][pos.x].color != color or board.board[pos.y - 2][pos.x].is_free_point()):
                neighbors.append(Position(pos.x, pos.y - 1))
        elif curr_case.is_point and curr_case.color == color and not curr_case.is_connected:
            return (True, [Position(pos.x, pos.y - 1)])

    # Vérification de la case à droite
    if pos.x + 1 < board.height:
        curr_case = board.board[pos.y][pos.x + 1]
        if not curr_case.color:
            if (pos.x + 2 >= board.width or board.board[pos.y][pos.x + 2].color != color or board.board[pos.y][pos.x + 2].is_free_point()) \
                    and (pos.y - 1 < 0 or board.board[pos.y - 1][pos.x + 1].color != color or board.board[pos.y - 1][pos.x + 1].is_free_point()) \
                    and (pos.y + 1 >= board.height or board.board[pos.y + 1][pos.x + 1].color != color or board.board[pos.y + 1][pos.x + 1].is_free_point()):
                neighbors.append(Position(pos.x + 1, pos.y))
        elif curr_case.is_point and curr_case.color == color and not curr_case.is_connected:
            return (True, [Position(pos.x + 1, pos.y)])

    # Vérification de la case en bas
    if pos.y + 1 < board.width:
        curr_case = board.board[pos.y + 1][pos.x]
        if not curr_case.color:
            if (pos.x - 1 < 0 or board.board[pos.y + 1][pos.x - 1].color != color or board.board[pos.y + 1][pos.x - 1].is_free_point()) \
                    and (pos.x + 1 >= board.width or board.board[pos.y + 1][pos.x + 1].color != color or board.board[pos.y + 1][pos.x + 1].is_free_point()) \
                    and (pos.y + 2 >= board.height or board.board[pos.y + 2][pos.x].color != color or board.board[pos.y + 2][pos.x].is_free_point()):
                neighbors.append(Position(pos.x, pos.y + 1))
        elif curr_case.is_point and curr_case.color == color and not curr_case.is_connected:
            return (True, [Position(pos.x, pos.y + 1)])
    return (False, neighbors)

def dfs_for_all_path(board, pos, color, current_path, all_paths, opti, all_shortest_paths):
    current_path.append(pos)

    test, neighbors = neighboring_available_cases(board, pos, color)

    if test:
        current_path.append(neighbors[0])
        if opti.check_reachable.value >= CheckReachable.END_PATH.value:
            if opti.reachability_check_method == ReachabilityCheckMethod.SHORTEST_PATH_FIRST:
                if is_all_colors_reachable_shortest_paths_first(board, all_shortest_paths):
                    all_paths.append((current_path.copy()))
            elif is_all_colors_reachable(board, color):
                all_paths.append((current_path.copy()))            

        current_path.pop()
    else:
        for pos in neighbors:
            board.board[pos.y][pos.x].color = color
            if (opti.check_reachable == CheckReachable.NEAR_2_POINTS and count_points_around(board, pos) >= 2) \
                or (opti.check_reachable == CheckReachable.EVERY_CASE) \
                or (opti.check_reachable == CheckReachable.NEAR_3_THINGS and count_things_around(board, pos) >= 3):
                if opti.reachability_check_method == ReachabilityCheckMethod.SHORTEST_PATH_FIRST:
                    if is_all_colors_reachable_shortest_paths_first(board, all_shortest_paths):
                        dfs_for_all_path(board, pos, color, current_path, all_paths, opti, all_shortest_paths)
                elif is_all_colors_reachable(board, color):
                    dfs_for_all_path(board, pos, color, current_path, all_paths, opti, all_shortest_paths)
            else:
                dfs_for_all_path(board, pos, color, current_path, all_paths, opti, all_shortest_paths)
                
            board.board[pos.y][pos.x].color = ""

    current_path.pop()

def create_all_paths(board, opti):
    all_paths = []
    
    all_shortest_paths = {}
    if opti.reachability_check_method == ReachabilityCheckMethod.SHORTEST_PATH_FIRST:
        all_shortest_paths = find_all_shortest_paths(board)
    # print(all_shortest_paths)
    
    # Print the is_connected status for each cell in the board
    # print("Initial is_connected status for the board:")
    # for y in range(board.height):
    #     for x in range(board.width):
    #         print(f"Position ({x}, {y}): is_connected = {board.board[y][x].is_connected}")
    for color in board.pos_points:

        color_paths = []
        curr_color_pos = Position(board.pos_points[color][0].x, board.pos_points[color][0].y)
        board.board[curr_color_pos.y][curr_color_pos.x].is_connected = True

        dfs_for_all_path(board, curr_color_pos, color, [], color_paths, opti, all_shortest_paths)
        
        all_paths.append(color_paths.copy())
        board.board[curr_color_pos.y][curr_color_pos.x].is_connected = False

    return all_paths



def find_and_apply_valid_combinations(board, all_paths, opti):
    """
    Find and apply valid combinations of paths on the board.
    """
    valid_combos = find_valid_combinations_with_board(all_paths, len(all_paths), [], 0, [], board, opti)
    apply_valid_combinations(board, valid_combos)


def apply_valid_combinations(board, valid_combos):
    """
    Apply valid combinations of paths on the board.
    """
    for combo in valid_combos:
        for path in combo:
            color = board.board[path[0].y][path[0].x].color  # Couleur du premier point du chemin

            for pos in path:
                board.board[pos.y][pos.x].color = color  # Mise à jour de la couleur sur la planche


def find_valid_combinations_with_board(all_paths, nb_paths, current_combo, index, valid_combos, board, opti):
    """
    Recursively find valid combinations of paths.
    """
    if index == nb_paths:
        valid_combos.append(current_combo.copy())
        return

    for path in all_paths[index]:
        # Vérifier si chaque élément de path dans la board a une couleur vide
        if all(board.board[pos.y][pos.x].color == "" for pos in path[1:-1]):

            curr_color = board.board[path[0].y][path[0].x].color
            if index == 0 or opti.check_reachable.value < CheckReachable.END_PATH.value \
            or is_all_colors_list_reachable(board, current_combo + [path]):
            
                # Ajouter chaque élément de path à la board
                for pos in path[1:-1]:
                    board.board[pos.y][pos.x].color = curr_color
                board.board[path[-1].y][path[-1].x].is_connected = True  # Connecter le dernier point du chemin
                board.board[path[0].y][path[0].x].is_connected = True    # Connecter le premier point du chemin

                # Appel récursif
                current_combo.append(path)
                find_valid_combinations_with_board(all_paths, nb_paths, current_combo, index + 1, valid_combos, board, opti)
                current_combo.pop()

                # Retirer chaque élément de path de la board après l'appel récursif
                for pos in path[1:-1]:
                    board.board[pos.y][pos.x].color = ""  # Réinitialiser la couleur à vide
                board.board[path[-1].y][path[-1].x].is_connected = False  # Déconnecter le dernier point du chemin
                board.board[path[0].y][path[0].x].is_connected = False    # Déconnecter le premier point du chemin

    return valid_combos
