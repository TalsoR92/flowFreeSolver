from Toitoine.board.board import *
from Toitoine.solver.tools import *

def extends_path(board):
    is_changed = True
    ch = False
    while is_changed and board.len_points > 0:
        is_changed = False
        i = 0
        while i < board.len_points:
            x, y = board.points[i]
            m = ' '
            c = 0
            # si il est un seul chemin ou espace y aller
            if my_color(board, (x, y)):
                #i += 1
                is_changed = True
                ch = True
                continue
            
            if is_no_color(board, (x,y)):#si c'est une non_couleur
                if x > 0:# il reste a savoir si un chemin est compatible a un autre
                    if board.M[x-1][y] == "" or (is_point(board, (x-1, y)) and path_is_link(board, (x, y), (x-1, y))):
                        m = 'u'
                        c += 1

                if x < board.size-1:
                    if board.M[x+1][y] == "" or (is_point(board, (x+1, y)) and path_is_link(board, (x, y), (x+1, y))):
                        m = 'd'
                        c += 1
                        
                if y > 0:
                    if board.M[x][y-1] == "" or (is_point(board, (x, y-1)) and path_is_link(board, (x, y), (x, y-1))):
                        m = 'l'
                        c += 1
                        
                if y < board.size-1:
                    if board.M[x][y+1] == "" or (is_point(board, (x, y+1)) and path_is_link(board, (x, y), (x, y+1))):
                        m = 'r'
                        c += 1
            else:#si c'est une coulleur
                if x > 0:# il reste a savoir si un chemin est compatible a un autre
                    if board.M[x-1][y] == "" or (is_no_color(board, (x-1, y)) and is_point(board, (x-1, y)) and path_is_link(board, (x, y), (x-1, y))):
                        m = 'u'
                        c += 1

                if x < board.size-1:
                    if board.M[x+1][y] == "" or (is_no_color(board, (x+1, y)) and is_point(board, (x+1, y)) and path_is_link(board, (x, y), (x+1, y))):
                        m = 'd'
                        c += 1
                        
                if y > 0:
                    if board.M[x][y-1] == "" or (is_no_color(board, (x, y-1)) and is_point(board, (x, y-1)) and path_is_link(board, (x, y), (x, y-1))):
                        m = 'l'
                        c += 1
                        
                if y < board.size-1:
                    if board.M[x][y+1] == "" or (is_no_color(board, (x, y+1)) and is_point(board, (x, y+1)) and path_is_link(board, (x, y), (x, y+1))):
                        m = 'r'
                        c += 1
            
            if c == 1:
                move(board, (x, y), m)
                is_changed = True
                ch = True
                continue
            i += 1
    return ch
