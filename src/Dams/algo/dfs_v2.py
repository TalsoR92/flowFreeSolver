from Dams.class_files.Board import *
from Dams.printer.printer import *
from Dams.algo.opti_v1 import *
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


def dfs_dot_all_path(board, pos, color, current_path, all_paths):
    current_path.append(pos)

    test, neighbors = neighboring_available_cases(board, pos, color)
    # print(f"pos = {pos} and neighbors = {neighbors}")
    if test:  # and is_all_colors_reachable(board):
        current_path.append(neighbors[0])

        if is_all_colors_reachable(board, color):
            all_paths.append((current_path.copy()))

        current_path.pop()
    else:
        for pos in neighbors:
            # print(f" chosen = {pos} || curr_path = {current_path} \n")

            board.board[pos.y][pos.x].color = color
            dfs_dot_all_path(board, pos, color, current_path, all_paths)
            board.board[pos.y][pos.x].color = ""

    current_path.pop()


def create_all_paths(board):
    all_paths = []
    start = 4
    print(f"nb color : {len(board.pos_points)}")
    for color in board.pos_points:
        print(f"color = {color} || pos = {board.pos_points[color]}")
        color_paths = []
        curr_color_pos = Position(board.pos_points[color][0].x, board.pos_points[color][0].y)
        board.board[curr_color_pos.y][curr_color_pos.x].is_connected = True
        # print(color)
        dfs_dot_all_path(board, curr_color_pos, color, [], color_paths)
        
        all_paths.append(deepcopy(color_paths))
    print("sahhhh")
    print(f"nb list : {count_second_level_lists(all_paths)}\n\n")
    print(all_paths)

    res = find_valid_combinations(all_paths)
    print()
    print(f"nb list : {len(res)}\n\n")
    print("find_valid_combinations(all_paths)")
    print(res)
    # print(board.board[0][1].color)
    # print(f"first color : {board.pos_points['#']}")

    apply_valid_combinations(board, res)

def paths_intersect(path1, path2):
    """
    Check if two paths intersect.
    """
    for pos in path1:
        if pos in path2:
            return True
    return False

def find_valid_combinations(all_paths, current_combo=[], index=0, valid_combos=[]):
    """
    Recursively find valid combinations of paths.
    """
    if index == len(all_paths):
        valid_combos.append(current_combo.copy())
        return

    for path in all_paths[index]:
        if all(not paths_intersect(path, other_path) for other_path in current_combo):
            current_combo.append(path)
            find_valid_combinations(all_paths, current_combo, index + 1, valid_combos)
            current_combo.pop()

    return valid_combos

def count_second_level_lists(lst):
    """
    Count the number of lists at the second level in a list of lists of lists.

    Parameters:
        lst (list): The list of lists of lists.

    Returns:
        int: The number of lists at the second level.
    """
    count = 0
    for sublist in lst:
        for item in sublist:
            if isinstance(item, list):
                count += 1
    return count


def apply_valid_combinations(board, valid_combos):
    """
    Apply valid combinations of paths on the board.
    """
    for combo in valid_combos:
        for path in combo:
            color = board.board[path[0].y][path[0].x].color  # Couleur du premier point du chemin
            print(f"pos = {path[0]}  ||  color = {color}")
            for pos in path:
                board.board[pos.y][pos.x].color = color  # Mise à jour de la couleur sur la planche
