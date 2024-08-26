from Dams.class_files.Board import *
from Dams.printer.printer import *
from Dams.algo.dfs_on_board import *
from Dams.include import *
from typing import List, Any, Tuple, Deque, Dict, Optional
from collections import deque
import bisect
from copy import deepcopy

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
            if not curr_case.color:
                board.board[curr_pos.y][curr_pos.x].color = "tmp"
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    if pos.y - 1 >= 0:
        curr_pos = Position(pos.x, pos.y - 1)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if not curr_case.color:
                board.board[curr_pos.y][curr_pos.x].color = "tmp"
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    if pos.x + 1 < board.width:
        curr_pos = Position(pos.x + 1, pos.y)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if not curr_case.color:
                board.board[curr_pos.y][curr_pos.x].color = "tmp"
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    if pos.y + 1 < board.height:
        curr_pos = Position(pos.x, pos.y + 1)
        curr_case = board.board[curr_pos.y][curr_pos.x]
        if not curr_case.is_point:
            if not curr_case.color:
                board.board[curr_pos.y][curr_pos.x].color = "tmp"
                queue.append(path + [curr_pos])
        elif curr_case.is_right_point(color):
            return path + [curr_pos]

    return []
    
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
            board.board[start_pos.y][start_pos.x].is_connected = False
            return res

    board.board[start_pos.y][start_pos.x].is_connected = True
    # Si aucun chemin n'a été trouvé, retourner None
    return []

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
        clear_tmp_color(board) # Clear 'tmp' colors after each BFS search

    return shortest_paths

