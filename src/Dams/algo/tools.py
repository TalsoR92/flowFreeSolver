from Dams.class_files.Board import *
from Dams.printer.printer import *
from Dams.algo.dfs_on_board import *
from Dams.include import *
from typing import List, Any, Tuple, Deque, Dict, Optional
from collections import deque
import bisect
from copy import deepcopy

def count_points_around(board, pos):
    """
    Count the number of points around a given position on the board.
    """
    count = 0
    if pos.y > 0:
        if board.board[pos.y - 1][pos.x].is_point:
            count += 1
        if pos.x < board.width - 1 and board.board[pos.y - 1][pos.x + 1].is_point:
            count += 1
        if pos.x > 0 and board.board[pos.y - 1][pos.x - 1].is_point:
            count += 1
    if pos.y < board.height - 1:
        if board.board[pos.y + 1][pos.x].is_point:
            count += 1
        if pos.x < board.width - 1 and board.board[pos.y + 1][pos.x + 1].is_point:
            count += 1
        if pos.x > 0 and board.board[pos.y + 1][pos.x - 1].is_point:
            count += 1
    if pos.x < board.width - 1 and board.board[pos.y][pos.x + 1].is_point:
        count += 1
    if pos.x > 0 and board.board[pos.y][pos.x - 1].is_point:
        count += 1
    # print(count)
    # print(f"pos: {pos}")
    # if count >= 2:
    #     print(board)
    return count


def count_things_around(board, pos):
    """
    Count the number of points or border around a given position on the board.
    """
    count = 0
    border = False
    if pos.y > 0:
        if board.board[pos.y - 1][pos.x].is_point:
            count += 1
        if pos.x < board.width - 1 and board.board[pos.y - 1][pos.x + 1].is_point:
            count += 1
        if pos.x > 0 and board.board[pos.y - 1][pos.x - 1].is_point:
            count += 1
    else:
        border = True
    if pos.y < board.height - 1:
        if board.board[pos.y + 1][pos.x].is_point:
            count += 1
        if pos.x < board.width - 1 and board.board[pos.y + 1][pos.x + 1].is_point:
            count += 1
        if pos.x > 0 and board.board[pos.y + 1][pos.x - 1].is_point:
            count += 1
    else:
        border = True
    if pos.x < board.width - 1:
        if board.board[pos.y][pos.x + 1].is_point:
            count += 1
    else:
        border = True
    if pos.x > 0:
        if board.board[pos.y][pos.x - 1].is_point:
            count += 1
    else:
        border = True
    # print(count)
    # print(f"pos: {pos}")
    # if count >= 2:
    #     print(board)
    return count + int(border)

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