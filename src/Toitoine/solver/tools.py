from Toitoine.board.board import *

def is_link(board, p1, p2):
    if is_no_color(board, p1):
        x, y = p2
        union_color(board, p1, board.M[x][y])
    else:
        x, y = p1
        union_color(board, p2, board.M[x][y])
    board.points.remove(p1)
    board.points.remove(p2)
    board.len_points -= 2

def has_2color(board, p, color):
    x, y = p
    c = 0
    if x > 0 and board.M[x-1][y] == color:
        c += 1
    if x < board.size-1 and board.M[x+1][y] == color:
        c += 1
    if y > 0 and board.M[x][y-1] == color:
        c += 1
    if y < board.size-1 and board.M[x][y+1] == color:
        c += 1
    
    if c > 1:
        return False
    return True

def path_is_link2(board, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if (not has_2color(board, p1, board.M[x2][y2])) or (not has_2color(board, p2, board.M[x1][y1])):
        return False
    if x1 == x2:
        if x1 > 0 and board.M[x1-1][y1] == board.M[x1][y1]:
            if board.M[x2][y2] == board.M[x2-1][y2]:
                return False

        elif x1 < board.size-1 and board.M[x1+1][y1] == board.M[x1][y1]:
            if board.M[x2][y2] == board.M[x2+1][y2]:
                return False

    elif y1 == y2:
        if y1 > 0 and board.M[x1][y1-1] == board.M[x1][y1]:
            if board.M[x2][y2] == board.M[x2][y2-1]:
                return False

        elif y1 < board.size-1 and board.M[x1][y1+1] == board.M[x1][y1]:
            if board.M[x2][y2] == board.M[x2][y2+1]:
                return False

    return True

def path_is_link(board, p1, p2):
    x, y = p2
    u, v = p1
    if is_no_color(board, (x, y)) and board.M[x][y] == board.M[u][v]:
        return False
    if not path_is_link2(board, p1, p2):
        return False
    color = board.M[u][v]
    m = ' '
    nc = board.M[x][y]
    if x > 0 and board.M[x-1][y] == nc:
        m = 'u'
        x -= 1
    elif x < board.size-1 and board.M[x+1][y] == nc:
        m = 'd'
        x += 1
    elif y > 0 and board.M[x][y-1] == nc:
        m = 'l'
        y -= 1
    elif y < board.size-1 and board.M[x][y+1] == nc:
        m = 'r'
        y += 1

    while True:
        if x > 0 and m != 'd' and board.M[x-1][y] == nc:
            m = 'u'
            if y > 0 and board.M[x][y-1] == color:
                return False
            if y < board.size-1 and board.M[x][y+1] == color:
                return False
            x -= 1
        elif x < board.size-1 and m != 'u' and board.M[x+1][y] == nc:
            m = 'd'
            if y > 0 and board.M[x][y-1] == color:
                return False
            if y < board.size-1 and board.M[x][y+1] == color:
                return False
            x += 1
        elif y > 0 and m != 'r' and board.M[x][y-1] == nc:
            m = 'l'
            if x > 0 and board.M[x-1][y] == color:
                return False
            if x < board.size-1 and board.M[x+1][y] == color:
                return False
            y -= 1
        elif y < board.size-1 and m != 'l' and board.M[x][y+1] == nc:
            m = 'r'
            if x > 0 and board.M[x-1][y] == color:
                return False
            if x < board.size-1 and board.M[x+1][y] == color:
                return False
            y += 1
        else:
            if x > 0 and board.M[x-1][y] == color and not is_point(board, (x-1,y)):
                return False
            if x < board.size-1 and board.M[x+1][y] == color and not is_point(board, (x+1,y)):
                return False
            if y > 0 and board.M[x][y-1] == color and not is_point(board, (x,y-1)):
                return False
            if y < board.size-1 and board.M[x][y+1] == color and not is_point(board, (x,y+1)):
                return False
            return True

'''def path_not_have_this_color(board, p, color):
    c = ' '
    x, y = p
    col = board.M[x][y]
    while True:
        if board.M[x+1][y] == color or board.M[x-1][y] == color or board.M[x][y+1] == color or board.M[x][y-1] == color:
            return False
        if c != 'u' and x > 0:
            pass'''

def nb_color(board, mov, p):
    x, y = p
    if board.M[x][y] == '':
        return False
    c = 0
    if mov == 'd' and x-1 > 0 and is_point(board, (x-1, y)):
        c += 1
    if mov == 'u' and x+1 < board.size-1 and board.M[x][y] == '' and is_point(board, (x+1, y)):
        c += 1
    if mov == 'l' and y-1 > 0 and board.M[x][y] == '' and is_point(board, (x, y-1)):
        c += 1
    if mov == 'r' and y+1 < board.size-1 and board.M[x][y] == '' and is_point(board, (x, y+1)):
        c += 1
    return c

def is_fall(board, p1, p2):# ajouter le nb_color
    '''
    return True si il y a un mur entre p1 et p2
    sinon False
    '''
    x1, y1 = p1
    x2, y2 = p2
    color = board.M[x2][y2]
    if color == "":
        return False
    if x1 != board.size-1 and y1 != board.size-1 and \
        board.M[x1+1][y1] == color and board.M[x1+1][y1+1] == color and board.M[x1][y1+1] == color:
        return True
    if x1 != 0 and y1 != board.size-1 and \
         board.M[x1-1][y1] == color and board.M[x1-1][y1+1] == color and board.M[x1][y1+1] == color:
        return True
    if x1 != 0 and y1 != 0 and \
        board.M[x1][y1-1] == color and board.M[x1-1][y1-1] == color and board.M[x1-1][y1] == color:
        return True
    if x1 != board.size-1 and y1 != 0 and \
        board.M[x1][y1-1] == color and board.M[x1+1][y1-1] == color and board.M[x1+1][y1] == color:
        return True
    # si il y a une couleur mais pas de point c'est un mur
    if p2 not in board.points:
        return True
    # c'est un point et qu'il ne peut pas parandre la case de p1
    if x2 > 0 and x1 > x2:#up
        if y2 > 0 and is_point(board, (x2-1, y2-1)) and board.M[x2-1][y2-1] != color and \
            board.M[x2][y2-1] != board.M[x2-1][y2-1] and board.M[x2][y2-1] != board.M[x2-1][y2-1]:
            if  (x2-1 == 0 and y2-1 == 0) or \
                ((y2-1 == 0 or board.M[x2][y2-2] != "" and not is_point(board, (x2, y2-2))) and \
                (x2-1 == 0 or board.M[x2-2][y2] != "" and not is_point(board, (x2-2, y2)))):
                return True

        elif y2 > board.size and is_point(board, (x2-1, y2+1)) and board.M[x2-1][y2+1] != color and \
            board.M[x2][y2+1] != board.M[x2-1][y2+1] and board.M[x2][y2+1] != board.M[x2-1][y2+1]:
            if  (x2-1 == 0 and y2+1 == board.size-1) or \
                ((y2+1 == board.size-1 or board.M[x2][y2+2] != "" and not is_point(board, (x2, y2+2))) and \
                (x2-1 == 0 or board.M[x2-2][y2] != "" and not is_point(board, (x2-2, y2)))):
                return True

    elif x2 < board.size-1 and x1 < x2:#down
        if y2 < 0 and is_point(board, (x2+1, y2-1)) and board.M[x2+1][y2-1] != color and \
            board.M[x2][y2+1] != board.M[x2+1][y2-1] and board.M[x2][y2-1] != board.M[x2+1][y2-1]:
            if  (x2+1 == board.size-1 and y2-1 == 0) or \
                ((y2-1 == 0 or board.M[x2][y2-2] != "" and not is_point(board, (x2, y2-2))) and \
                (x2+1 == board.size-1 or board.M[x2+2][y2] != "" and not is_point(board, (x2+2, y2)))):
                return True

        elif y2 > board.size and is_point(board, (x2+1, y2+1)) and board.M[x2+1][y2+1] != color and \
            board.M[x2][y2+1] != board.M[x2+1][y2+1] and board.M[x2][y2+1] != board.M[x2+1][y2+1]:
            if  (x2+1 == board.size-1 and y2+1 == board.size-1) or \
                ((y2+1 == board.size-1 or board.M[x2][y2+2] != "" and not is_point(board, (x2, y2+2)))) and \
                (x2+1 == board.size-1 or board.M[x2+2][y2] != "" and not is_point(board, (x2+2, y2))):
                return True

    elif y2 > 0 and y1 > y2:#left
        if x2 > 0 and is_point(board, (x2+1, y2-1)) and board.M[x2+1][y2-1] != color and \
            board.M[x2][y2-1] != board.M[x2-1][y2-1] and board.M[x2][y2-1] != board.M[x2-1][y2-1]:
            if  (x2+1 == board.size-1 and y2-1 == 0) or \
                ((y2-1 == 0 or board.M[x2][y2-2] != "" and not is_point(board, (x2, y2-2))) and \
                (x2+1 == board.size-1 or board.M[x2+2][y2] != "" and not is_point(board, (x2+2, y2)))):
                return True
            
        elif x2 < board.size-1 and is_point(board, (x2-1, y2-1)) and board.M[x2-1][y2-1] != color and \
            board.M[x2][y2-1] != board.M[x2+1][y2-1] and board.M[x2][y2-1] != board.M[x2+1][y2-1]:
            if  (x2-1 == 0 and y2-1 == 0) or \
                ((y2-1 == 0 or board.M[x2][y2-2] != "" and not is_point(board, (x2, y2-2))) and \
                (x2-1 == 0 or board.M[x2-2][y2] != "" and not is_point(board, (x2-2, y2)))):
                return True

    elif y2 < board.size-1 and y1 < y2:#right
        if x2 > 0 and is_point(board, (x2+1, y2+1)) and board.M[x2+1][y2+1] != color and \
            board.M[x2][y2+1] != board.M[x2-1][y2+1] and board.M[x2][y2+1] != board.M[x2-1][y2+1]:
            if  (x2+1 == board.size-1 and y2+1 == board.size-1) or \
                ((y2+1 == board.size-1 or board.M[x2][y2+2] != "" and not is_point(board, (x2, y2+2))) and \
                (x2+1 == board.size-1 or board.M[x2+2][y2] != "" and not is_point(board, (x2+2, y2)))):
                return True
            
        elif x2 < board.size-1 and is_point(board, (x2-1, y2+1)) and board.M[x2-1][y2+1] != color and \
            board.M[x2][y2+1] != board.M[x2+1][y2+1] and board.M[x2][y2+1] != board.M[x2+1][y2+1]:
            if  (x2-1 == 0 and y2+1 == board.size-1) or \
                ((y2+1 == board.size-1 or board.M[x2][y2+2] != "" and not is_point(board, (x2, y2+2))) and \
                (x2-1 == 0 or board.M[x2-2][y2] != "" and not is_point(board, (x2-2, y2)))):#here
                return True

    return False

def is_point(board, p):
    return p in board.points

def union_color(board, p, color):
    '''
    change toutes les couleurs de p en color dans la board
    '''
    x,y = p
    colorp = board.M[x][y]
    while True:
        board.M[x][y] = color
        if x == 0:
            if y == 0:#|-
                if board.M[x+1][y] == colorp:
                    x += 1
                elif board.M[x][y+1] == colorp:
                    y += 1
                else:
                    return
            elif y == board.size-1:#-|
                if board.M[x+1][y] == colorp:
                    x += 1
                elif board.M[x][y-1] == colorp:
                    y -= 1
                else:
                    return
            else:#-
                if board.M[x+1][y] == colorp:
                    x += 1
                elif board.M[x][y-1] == colorp:
                    y -= 1
                elif board.M[x][y+1] == colorp:
                    y += 1
                else:
                    return

        elif x == board.size-1:#
            if y == 0:#|_
                if board.M[x-1][y] == colorp:
                    x -= 1
                elif board.M[x][y+1] == colorp:
                    y += 1
                else:
                    return

            elif y == board.size-1:#_|
                if board.M[x-1][y] == colorp:
                    x -= 1
                elif board.M[x][y-1] == colorp:
                    y -= 1
                else:
                    return
            else:#_
                if board.M[x-1][y] == colorp:
                    x -= 1
                elif board.M[x][y-1] == colorp:
                    y -= 1
                elif board.M[x][y+1] == colorp:
                    y += 1
                else:
                    return

        else:#
            if y == 0:#|.
                if board.M[x+1][y] == colorp:
                    x += 1
                elif board.M[x-1][y] == colorp:
                    x -= 1
                elif board.M[x][y+1] == colorp:
                    y += 1
                else:
                    return
            elif y == board.size-1:#.|
                if board.M[x+1][y] == colorp:
                    x += 1
                elif board.M[x-1][y] == colorp:
                    x -= 1
                elif board.M[x][y-1] == colorp:
                    y -= 1
                else:
                    return
            else:#.
                if board.M[x+1][y] == colorp:
                    x += 1
                elif board.M[x-1][y] == colorp:
                    x -= 1
                elif board.M[x][y+1] == colorp:
                    y += 1
                elif board.M[x][y-1] == colorp:
                    y -= 1
                else:
                    return

def new_no_color(board):
    '''
    crée une nouvelle couleur et renvois sa représentation en string
    '''
    board.no_color += 1
    return "no_color"+str(board.no_color)

def update_val_point(board, actual, new):
    for i in range(len(board.points)):
        if board.points[i] == actual:
            board.points[i] = new
            return True
    return False

def move(board, p, mov):
    x, y = p
    if mov == 'd':
        if is_point(board, (x+1,y)):
            is_link(board, p, (x+1, y))
        else:
            board.M[x+1][y] = board.M[x][y]
            update_val_point(board, p, ((x+1, y)))
    elif mov == 'u':
        if is_point(board, (x-1,y)):
            is_link(board, p, (x-1, y))
        else:
            board.M[x-1][y] = board.M[x][y]
            update_val_point(board, p, ((x-1, y)))
    elif mov == 'l':
        if is_point(board, (x,y-1)):
            is_link(board, p, (x, y-1))
        else:
            board.M[x][y-1] = board.M[x][y]
            update_val_point(board, p, ((x, y-1)))
    elif mov == 'r':
        if is_point(board, (x,y+1)):
            is_link(board, p, (x, y+1))
        else:
            board.M[x][y+1] = board.M[x][y]
            update_val_point(board, p, ((x, y+1)))

def my_color(board, p):
    x, y = p
    if is_no_color(board, p):
        return False
    color = board.M[x][y]
    if x < board.size-1 and board.M[x+1][y] == color and is_point(board, (x+1,y)):
        board.points.remove(p)
        board.points.remove((x+1, y))
        board.len_points -= 2
        return True
    if x > 0 and board.M[x-1][y] == color and is_point(board, (x-1,y)):
        board.points.remove(p)
        board.points.remove((x-1, y))
        board.len_points -= 2
        return True
    if y > 0 and board.M[x][y-1] == color and is_point(board, (x,y-1)):
        board.points.remove(p)
        board.points.remove((x, y-1))
        board.len_points -= 2
        return True
    if y < board.size-1 and board.M[x][y+1] == color and is_point(board, (x,y+1)):
        board.points.remove(p)
        board.points.remove((x, y+1))
        board.len_points -= 2
        return True
    return False

def is_free(board, p):
    x, y = p
    if board.M[x][y] == "":
        return True
    if is_no_color(board, p) and is_point(board, p):
        return True
    return False

def is_no_color(board, p):
    x, y = p
    s = board.M[x][y]
    return "no_color" in s
