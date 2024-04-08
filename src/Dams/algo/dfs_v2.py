# def create_all_path(board,):
from Dams.class_files.Board import *

def available_cases_for_dfs_v2(board, pos, color, visited):
    neighbors = []
    if pos.x - 1 >= 0 and Position(pos.x - 1, pos.y) not in visited:
        if board.board[pos.y][pos.x - 1] is None:
            neighbors.append(Position(pos.x - 1, pos.y))
        elif isinstance(board.board[pos.y][pos.x - 1], Point) and board.board[pos.y][pos.x - 1].color == color and not board.board[pos.y][pos.x - 1].connected:
            return (True, [Position(pos.x - 1, pos.y)])

    if pos.y - 1 >= 0 and Position(pos.x, pos.y - 1) not in visited:
        if board.board[pos.y - 1][pos.x] is None:
            neighbors.append(Position(pos.x, pos.y - 1))
        elif isinstance(board.board[pos.y - 1][pos.x], Point) and board.board[pos.y - 1][pos.x].color == color and not board.board[pos.y - 1][pos.x].connected:
            return (True, [Position(pos.x, pos.y - 1)])

    if pos.x + 1 < len(board.board[0]) and Position(pos.x + 1, pos.y) not in visited:
        if board.board[pos.y][pos.x + 1] is None:
            neighbors.append(Position(pos.x + 1, pos.y))
        elif isinstance(board.board[pos.y][pos.x + 1], Point) and board.board[pos.y][pos.x + 1].color == color and not board.board[pos.y][pos.x + 1].connected:
            return (True, [Position(pos.x + 1, pos.y)])

    if pos.y + 1 < len(board.board) and Position(pos.x, pos.y + 1) not in visited:
        if board.board[pos.y + 1][pos.x] is None:
            neighbors.append(Position(pos.x, pos.y + 1))
        elif isinstance(board.board[pos.y + 1][pos.x], Point) and board.board[pos.y + 1][pos.x].color == color and not board.board[pos.y + 1][pos.x].connected:
            return (True, [Position(pos.x, pos.y + 1)])

    return (False, neighbors)



def dot_all_path(board):
    all_paths = []
    print(board.board[0][0].color)
    dfs_dot_all_path(board, Position(0,0), board.board[0][0].color, [], all_paths)
    print(all_paths)


def dfs_dot_all_path(board, pos, color, current_path, all_paths):
    current_path.append(pos)

    test, neighbors = available_cases_for_dfs_v2(board, pos, color, current_path)

    if test:
        current_path.append(neighbors[0])
        all_paths.append((current_path.copy()))

    for pos in neighbors:
        dfs_dot_all_path(board, pos, color, current_path, all_paths)

    current_path.pop()



