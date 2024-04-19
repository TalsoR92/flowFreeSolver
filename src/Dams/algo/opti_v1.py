from Dams.class_files.Board import *
from Dams.printer.printer import *
from Dams.algo.dfs_v2 import *
from Dams.include import *
from typing import List, Any, Tuple, Deque, Dict, Optional
from collections import deque
import bisect
from copy import deepcopy

def find_all_shortest_paths(board: Board) -> Dict[str, List[Position]]:
    """
    Find the shortest paths from each point of different colors to their respective pairs using BFS.

    Returns:
        dict: A dictionary containing each color and its shortest path from the starting position to its pair.
              If no path exists for a color, its value will be None.
    """
    shortest_paths = {}
    
    # Parcourir tous les points de la board
    for color, points_pos in board.pos_points.items():
        shortest_path = find_shortest_path(board, points_pos[0], color)
        shortest_paths[color] = shortest_path
    
    return shortest_paths


def find_shortest_path(board: Board, start_pos: Position, color: str) -> List[Position]:
    """
    Find the shortest path from a point of the given color to its pair using BFS.
    """
    # Initialisation de la file pour la BFS
    queue = deque([[start_pos]])
    board.board[start_pos.y][start_pos.x].is_connected = True
    # Parcours BFS pour trouver le chemin le plus court
    while queue:
        curr_path = queue.popleft()

        # Appeler neighboring_available_cases pour mettre à jour la file avec les positions voisines
        res = find_neighbors_for_BFS(board, queue, curr_path[-1], color, curr_path)
        if res:
            return res
    # Si aucun chemin n'a été trouvé, retourner None
    return []

def find_neighbors_for_BFS(board: Board, queue: Deque[List[Position]], pos: Position, color: str, path: List[Position]) -> List[Position]:
    """
        Determines the available neighboring positions around a given position on the game board for a specific color.
        It updates their color and adds them to the queue to enable a breadth-first search for the shortest path.

        Returns:
            - If the neighboring point of the specified color is found adjacent to the given position, it returns
            the shortest path from the starting position to that point.
            - Otherwise, it implements the queue for further BFS traversal and returns nothing.
    """
    if pos.x - 1 >= 0:
        curr_pos = Position(pos.x-1, pos.y)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if curr_case.color != color:
                board.board[curr_pos.y][curr_pos.x].color = color
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    if pos.y - 1 >= 0:
        curr_pos = Position(pos.x, pos.y - 1)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if curr_case.color != color:
                board.board[curr_pos.y][curr_pos.x].color = color
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    if pos.x + 1 < board.width:
        curr_pos = Position(pos.x + 1, pos.y)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if curr_case.color != color:
                board.board[curr_pos.y][curr_pos.x].color = color
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    if pos.y + 1 < board.height:
        curr_pos = Position(pos.x, pos.y + 1)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if curr_case.color != color:
                board.board[curr_pos.y][curr_pos.x].color = color
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    return []

def is_all_colors_reachable(board: Board, expect_color: str="") -> bool:
    """
    Determine if all colors points on the board are reachable.
    je veux que la fonction parcours is_color_reachable pour chaque couleur presente dans une variable list de couleur de la fonction
    """
    for color, (pos1, pos2) in board.pos_points.items():
        if color != expect_color and not is_color_reachable(board, pos1, pos2, color):
            return False
    return True


def is_color_reachable(board: Board, start_pos: Position, end_pos: Position, color: str) -> bool:
    """
    Determine if the points of the specified color are reachable.
    """
    list_cases = [(start_pos, 0)]

    while list_cases:
        (curr_pos, _) = list_cases.pop(0)
        # print(board)
        if manhattan_distance(curr_pos, end_pos) == 1:
            clear_tmp_color(board)
            return True

        find_neighbors_heuristic(board, curr_pos, list_cases,end_pos)

    clear_tmp_color(board)
    return False  # Pair is not reachable


def find_neighbors_heuristic(board: Board, curr_pos: Position, list_cases: List[Tuple[Position, int]], end_pos: Position):
    """
    Find valid neighboring positions of a given position and update the list for heuristic-based traversal.

    Effect:
        Updates the colors of visited positions with the specified color.
        Sorts the list of cases to explore based on Manhattan distance from the end position.
    """
    if curr_pos.x - 1 >= 0:
        left_pos = Position(curr_pos.x - 1, curr_pos.y)
        left_case = board.board[left_pos.y][left_pos.x]
        if not left_case.color:
            left_case.color = "tmp"  # Ajoute la couleur à la case
            bisect.insort(list_cases, (left_pos, manhattan_distance(left_pos, end_pos)), key=lambda x: x[1])

    if curr_pos.y - 1 >= 0:
        top_pos = Position(curr_pos.x, curr_pos.y - 1)
        top_case = board.board[top_pos.y][top_pos.x]
        if not top_case.color:
            top_case.color = "tmp"  # Ajoute la couleur à la case
            bisect.insort(list_cases, (top_pos, manhattan_distance(top_pos, end_pos)), key=lambda x: x[1])

    if curr_pos.x + 1 < board.width:
        right_pos = Position(curr_pos.x + 1, curr_pos.y)
        right_case = board.board[right_pos.y][right_pos.x]
        if not right_case.color:
            right_case.color = "tmp"   # Ajoute la couleur à la case
            bisect.insort(list_cases, (right_pos, manhattan_distance(right_pos, end_pos)), key=lambda x: x[1])

    if curr_pos.y + 1 < board.height:
        bottom_pos = Position(curr_pos.x, curr_pos.y + 1)
        bottom_case = board.board[bottom_pos.y][bottom_pos.x]
        if not bottom_case.color:
            bottom_case.color = "tmp"   # Ajoute la couleur à la case
            bisect.insort(list_cases, (bottom_pos, manhattan_distance(bottom_pos, end_pos)), key=lambda x: x[1])


def manhattan_distance(pos1, pos2):
    """
    Calculate the Manhattan distance between two positions.
    """
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)

def clear_tmp_color(board):
    """
    Clear the color "tmp" from all cells on the board.
    """
    for row in board.board:
        for cell in row:
            if cell.color == "tmp":
                cell.color = ""
    