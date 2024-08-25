from Toitoine.board.board import *
from Toitoine.solver.tools import *

def force_path(board):
    i = 0
    is_change = False
    while i < board.len_points:
        x, y = board.points[i]
        if not is_no_color(board, (x,y)):
            i += 1
            continue
        c = 0
        if x > 0:
            if board.M[x-1][y] == "":
                m = 'u'
                c += 1

        if x < board.size-1:
            if board.M[x+1][y] == "":
                m = 'd'
                c += 1
                
        if y > 0:
            if board.M[x][y-1] == "":
                m = 'l'
                c += 1
                
        if y < board.size-1:
            if board.M[x][y+1] == "":
                m = 'r'
                c += 1
        
        if c == 1:
            move(board, (x, y), m)
            is_change = True
        i += 1
    return True