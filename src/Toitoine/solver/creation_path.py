from Toitoine.board.board import *
from Toitoine.solver.tools import *

def path_right_up(board, p):
    x,y = p
    if board.M[x][y-1] != "":
        board.M[x][y] = board.M[x][y-1]
        if board.M[x-1][y] != "":
            board.points.remove((x, y-1))
            board.points.remove((x-1, y))
            board.len_points -= 2
        else:
            board.M[x-1][y] = board.M[x][y-1]
            update_val_point(board, (x, y-1), (x-1, y))
    elif board.M[x-1][y] != "":
        board.M[x][y] = board.M[x-1][y]
        if board.M[x][y-1] != "":
            board.points.remove((x, y-1))
            board.points.remove((x-1, y))
            board.len_points -= 2
        else:
            board.M[x][y-1] = board.M[x-1][y]
            update_val_point(board, (x-1, y), (x, y-1))
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x-1][y] = c
        board.M[x][y-1] = c
        board.len_points += 2
        board.points.append((x-1, y))
        board.points.append((x, y-1))

def path_up_left(board, p):
    x,y = p
    if board.M[x][y+1] != "":
        board.M[x][y] = board.M[x][y+1]
        if board.M[x-1][y] != "":
            board.points.remove((x, y+1))
            board.points.remove((x-1, y))
            board.len_points -= 2
        else:
            board.M[x-1][y] = board.M[x][y+1]
            update_val_point(board, (x, y+1), (x-1, y))
    elif board.M[x-1][y] != "":
        board.M[x][y] = board.M[x-1][y]
        if board.M[x][y+1] != "":
            board.points.remove((x, y+1))
            board.points.remove((x-1, y))
            board.len_points -= 2
        else:
            board.M[x][y+1] = board.M[x-1][y]
            update_val_point(board, (x-1, y), (x, y+1))
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x-1][y] = c
        board.M[x][y+1] = c
        board.len_points += 2
        board.points.append((x-1, y))
        board.points.append((x, y+1))

def path_left_down(board, p):
    x,y = p
    if board.M[x][y+1] != "":
        board.M[x][y] = board.M[x][y+1]
        if board.M[x+1][y] != "":
            board.points.remove((x, y+1))
            board.points.remove((x+1, y))
            board.len_points -= 2
        else:
            board.M[x+1][y] = board.M[x][y+1]
            update_val_point(board, (x, y+1), (x+1, y))
    elif board.M[x+1][y] != "":
        board.M[x][y] = board.M[x+1][y]
        if board.M[x][y+1] != "":
            board.points.remove((x, y+1))
            board.points.remove((x+1, y))
            board.len_points -= 2
        else:
            board.M[x][y+1] = board.M[x+1][y]
            update_val_point(board, (x+1, y), (x, y+1))
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x+1][y] = c
        board.M[x][y+1] = c
        board.len_points += 2
        board.points.append((x+1, y))
        board.points.append((x, y+1))

def path_down_right(board, p):
    x,y = p
    if board.M[x][y-1] != "":
        board.M[x][y] = board.M[x][y-1]
        if board.M[x+1][y] != "":
            board.points.remove((x, y-1))
            board.points.remove((x+1, y))
            board.len_points -= 2
        else:
            board.M[x+1][y] = board.M[x][y-1]
            update_val_point(board, (x, y-1), (x+1, y))
    elif board.M[x+1][y] != "":
        board.M[x][y] = board.M[x+1][y]
        if board.M[x][y-1] != "":
            board.points.remove((x, y-1))
            board.points.remove((x+1, y))
            board.len_points -= 2
        else:
            board.M[x][y-1] = board.M[x+1][y]
            update_val_point(board, (x+1, y), (x, y-1))
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x+1][y] = c
        board.M[x][y-1] = c
        board.len_points += 2
        board.points.append((x+1, y))
        board.points.append((x, y-1))

def path_up(board, p):
    x,y = p
    if board.M[x-1][y] != "":
        board.M[x][y] = board.M[x-1][y]
        update_val_point(board,(x-1,y), p)
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x-1][y] = c
        board.points.append((x-1, y))
        board.points.append((x, y))
        board.len_points += 2

def path_down(board, p):
    x,y = p
    if board.M[x+1][y] != "":
        board.M[x][y] = board.M[x+1][y]
        update_val_point(board,(x+1,y), p)
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x+1][y] = c
        board.points.append((x+1, y))
        board.points.append((x, y))
        board.len_points += 2

def path_left(board, p):
    x,y = p
    if board.M[x][y-1] != "":
        board.M[x][y] = board.M[x][y-1]
        update_val_point(board,(x,y-1), p)
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x][y-1] = c
        board.points.append((x, y-1))
        board.points.append((x, y))
        board.len_points += 2

def path_right(board, p):
    x,y = p
    if board.M[x][y+1] != "":
        board.M[x][y] = board.M[x][y+1]
        update_val_point(board,(x,y+1), p)
    else:
        c = new_no_color(board)
        board.M[x][y] = c
        board.M[x][y+1] = c
        board.points.append((x, y+1))
        board.points.append((x, y))
        board.len_points += 2

def create_path_with_color(board, p):
    x, y = p
    if is_point(board, p):#not is_no_color(board, p) and 
        if x == 0:
            if y == 0:
                if is_free(board, (x, y+1)) and is_free(board, (x+1, y)):
                    if board.M[x][y+1] == "":
                        path_right(board, (x, y+1))
                    if board.M[x+1][y] == "":
                        path_down(board, (x+1, y))

            elif y == board.size-1:
                if is_free(board, (x, y-1)) and is_free(board, (x+1, y)):
                    if board.M[x][y-1] == "":
                        path_left(board, (x, y-1))
                    if board.M[x+1][y] == "":
                        path_down(board, (x+1, y))

            else:
                if is_fall(board, p, (x, y+1)):
                    if is_free(board, (x, y-1)) and is_free(board, (x+1, y)):
                        if y > 2 and board.M[x][y-1] == "":
                            path_left(board, (x, y-1))
                        if board.M[x+1][y] == "" and is_fall(board, (x+1, y), (x+1, y+1)):
                            path_down(board, (x+1, y))

                elif is_fall(board, p, (x, y-1)):
                    if is_free(board, (x, y+1)) and is_free(board, (x+1, y)):
                        if y < board.size-2 and board.M[x][y+1] == "":
                            path_right(board, (x, y+1))
                        if board.M[x+1][y] == "" and is_fall(board, (x+1, y), (x+1, y-1)):
                            path_down(board, (x+1, y))

        elif x == board.size-1:
            if y == 0:
                if is_free(board, (x, y+1)) and is_free(board, (x-1, y)):
                    if board.M[x][y+1] == "":
                        path_right(board, (x, y+1))
                    if board.M[x-1][y] == "":
                        path_up(board, (x-1, y))

            elif y == board.size-1:
                if is_free(board, (x, y-1)) and is_free(board, (x-1, y)):
                    if board.M[x][y-1] == "":
                        path_left(board, (x, y-1))
                    if board.M[x-1][y] == "":
                        path_up(board, (x-1, y))

            else:
                if is_fall(board, p, (x, y+1)):
                    if is_free(board, (x, y-1)) and is_free(board, (x-1, y)):
                        if y > 2 and board.M[x][y-1] == "":
                            path_left(board, (x, y-1))
                        if board.M[x-1][y] == "" and is_fall(board, (x-1, y), (x-1, y+1)):
                            path_up(board, (x-1), y)

                elif is_fall(board, p, (x, y-1)):
                    if is_free(board, (x, y+1)) and is_free(board, (x-1, y)):
                        if y < board.size-2 and board.M[x][y+1] == "":
                            path_right(board, (x, y+1))
                        if board.M[x-1][y] == "" and is_fall(board, (x-1, y), (x-1, y-1)):
                            path_up(board, (x-1, y))

        else:
            if y == 0:
                if is_fall(board, p, (x+1, y)):
                    if is_free(board, (x, y+1)) and is_free(board, (x-1, y)):
                        if board.M[x][y+1] == "" and is_fall(board, (x, y+1), (x+1, y+1)):
                            path_right(board, (x, y+1))
                        if x > 2 and board.M[x-1][y] == "":
                            path_up(board, (x-1, y))
                
                if is_fall(board, p, (x-1, y)):
                    if is_free(board, (x, y+1)) and is_free(board, (x+1, y)):
                        if board.M[x][y+1] == "" and is_fall(board, (x, y+1), (x-1, y+1)):
                            path_right(board, (x, y+1))
                        if x < board.size-2 and board.M[x+1][y] == "":
                            path_down(board, (x+1, y))

            elif y == board.size-1:
                if is_fall(board, p, (x+1, y)):
                    if is_free(board, (x, y-1)) and is_free(board, (x-1, y)):
                        if board.M[x][y-1] == "" and is_fall(board, (x, y-1), (x+1, y-1)):
                            path_left(board, (x, y-1))
                        if x > 2 and board.M[x-1][y] == "":
                            path_up(board, (x-1, y))
                
                if is_fall(board, p, (x-1, y)):
                    if is_free(board, (x, y-1)) and is_free(board, (x+1, y)):
                        if board.M[x][y-1] == "" and is_fall(board, (x, y-1), (x-1, y-1)):
                            path_left(board, (x, y-1))
                        if x < board.size-2 and board.M[x+1][y] == "":
                            path_down(board, (x+1, y))

            else:
                if is_fall(board, p, (x+1, y)):
                    if is_fall(board, p, (x, y+1)):
                        if is_free(board, (x, y-1)) and is_free(board, (x-1, y)):
                            if x > 2 and board.M[x-1][y] == "" and is_fall(board, (x-1,y), (x-1, y+1)):
                                path_up(board, (x-1, y))
                            if y > 2 and board.M[x][y-1] == "" and is_fall(board, (x, y-1), (x+1, y-1)):
                                path_left(board, (x, y-1))

                    elif is_fall(board, p, (x, y-1)):
                        if is_free(board, (x, y+1)) and is_free(board, (x-1, y)):
                            if x > 2 and board.M[x-1][y] == "" and is_fall(board, (x-1,y), (x-1, y-1)):
                                path_up(board, (x-1, y))
                            if y < board.size-2 and board.M[x][y+1] == "" and is_fall(board, (x, y+1), (x+1, y+1)):
                                path_right(board, (x, y+1))

                elif is_fall(board, p, (x-1, y)):
                    if is_fall(board, p, (x, y+1)):
                        if is_free(board, (x, y-1)) and is_free(board, (x+1, y)):
                            if x < board.size-2 and board.M[x+1][y] == "" and is_fall(board, (x+1,y), (x+1, y+1)):
                                path_down(board, (x+1, y))
                            if y > 2 and board.M[x][y-1] == "" and is_fall(board, (x, y-1), (x-1, y-1)):
                                path_left(board, (x, y-1))

                    elif is_fall(board, p, (x, y-1)):
                        if is_free(board, (x, y+1)) and is_free(board, (x+1, y)):
                            if x < board.size-2 and  board.M[x+1][y] == "" and is_fall(board, (x+1,y), (x+1, y-1)):
                                path_down(board, (x+1, y))
                            if y < board.size-2 and  board.M[x][y+1] == "" and is_fall(board, (x, y+1), (x-1, y+1)):
                                path_right(board, (x, y+1))

def creation_path(board, p):
    '''
    crée un chemin si il est sur une bordure
    return si path ((x1,y1), (x2,y2)) les point des extremitée du path
    sinon return none
    '''
    (x, y) = p
    if board.M[x][y] != "":
        create_path_with_color(board, p)
    else:
        if x == 0:
            if y == 0: # si on est sur une bordure en haut à gauche
                path_left_down(board, p)
            
            elif y == board.size - 1: # si on est sur une bordure en haut à droite
                path_down_right(board, p)

            else: # si on est sur une bordure en haut
                if is_fall(board, (x, y), (x, y+1)):
                    path_down_right(board, (x, y))
                    return True

                elif is_fall(board, (x, y), (x, y-1)):
                    path_left_down(board, (x, y))
                    return True

                elif board.M[x][y-1] ==  board.M[x][y+1] and is_point(board, (x,y-1)) and is_point(board, (x,y+1)):
                    board.M[x][y] = board.M[x][y-1]
                    board.points.remove((x, y+1))
                    board.points.remove((x, y-1))
                    board.len_points -= 2
                    return True
                
                elif board.M[x+1][y] != "" and not is_no_color(board, (x+1,y)):
                    if board.M[x][y+1] != "" and not is_no_color(board, (x,y+1)):
                        if board.M[x][y+1] == board.M[x+1][y]:
                            path_down_right(board, (x,y))
                            return True
                        else:
                            path_left(board, (x,y))
                            return True
                    elif board.M[x][y-1] != "":
                        if board.M[x][y-1] == board.M[x+1][y]:
                            path_left_down(board, (x,y))
                            return True
                        else:
                            path_right(board, (x,y))
                            return True

        elif x == board.size - 1:
            if y == 0: # si on est sur une bordure en bas à gauche
                path_up_left(board, (x, y))
                return True

            elif y == board.size - 1: # si on est sur une bordure en bas à droite
                path_right_up(board, (x, y))
                return True

            else: # si on est sur une bordure en bas
                if is_fall(board, (x, y), (x, y+1)):
                    path_right_up(board, (x, y))
                    return True

                elif is_fall(board, (x, y), (x, y-1)):
                    path_up_left(board, (x, y))
                    return True

                elif board.M[x][y-1] ==  board.M[x][y+1] and is_point(board, (x,y-1)) and is_point(board, (x,y+1)):
                    board.M[x][y] = board.M[x][y-1]
                    board.points.remove((x, y+1))
                    board.points.remove((x, y-1))
                    board.len_points -= 2
                    return True
                
                elif board.M[x-1][y] != "" and not is_no_color(board, (x-1,y)):
                    if board.M[x][y+1] != "" and not is_no_color(board, (x,y+1)):
                        if board.M[x][y+1] == board.M[x-1][y]:
                            path_right_up(board, (x,y))
                            return True
                        else:
                            path_left(board, (x,y))
                            return True
                    elif board.M[x][y-1] != "" and not is_no_color(board, (x,y-1)):
                        if board.M[x][y-1] == board.M[x-1][y]:
                            path_up_left(board, (x,y))
                            return True
                        else:
                            path_right(board, (x,y))
                            return True
                
        else:
            if y == 0: # si on est sur une bordure à gauche
                if is_fall(board, (x, y), (x+1, y)):
                    path_up_left(board, (x, y))
                    return True

                elif is_fall(board, (x, y), (x-1, y)):
                    path_left_down(board, (x, y))
                    return True

                elif board.M[x-1][y] ==  board.M[x+1][y] and is_point(board, (x-1,y)) and is_point(board, (x+1,y)):
                    board.M[x][y] = board.M[x-1][y]
                    board.points.remove((x+1, y))
                    board.points.remove((x-1, y))
                    board.len_points -= 2
                    return True
                
                elif board.M[x][y+1] != "" and not is_no_color(board, (x,y+1)):
                    if board.M[x+1][y] != "" and not is_no_color(board, (x+1,y)):
                        if board.M[x][y+1] == board.M[x+1][y]:
                            path_down_right(board, (x,y))
                            return True
                        else:
                            path_up(board, (x,y))
                            return True
                    elif board.M[x-1][y] != "" and not is_no_color(board, (x-1,y)):
                        if board.M[x][y+1] == board.M[x-1][y]:
                            path_right_up(board, (x,y))
                            return True
                        else:
                            path_down(board, (x,y))
                            return True


            elif y == board.size - 1: # si on est sur une bordure à droite
                if is_fall(board, (x, y), (x+1, y)):
                    path_right_up(board, (x,y))
                    return True

                elif is_fall(board, (x, y), (x-1, y)):
                    path_down_right(board, (x,y))
                    return True

                elif board.M[x-1][y] ==  board.M[x+1][y] and is_point(board, (x-1,y)) and is_point(board, (x+1,y)):
                    board.M[x][y] = board.M[x-1][y]
                    board.points.remove((x+1, y))
                    board.points.remove((x-1, y))
                    board.len_points -= 2
                    return True
                
                elif board.M[x][y-1] != "" and not is_no_color(board, (x,y-1)):
                    if board.M[x+1][y] != "" and not is_no_color(board, (x+1,y)):
                        if board.M[x][y-1] == board.M[x+1][y]:
                            path_left_down(board, (x,y))
                            return True
                        else:
                            path_up(board, (x,y))
                            return True
                    elif board.M[x-1][y] != "" and not is_no_color(board, (x-1,y)):
                        if board.M[x][y-1] == board.M[x-1][y]:
                            path_right_up(board, (x,y))
                            return True
                        else:
                            path_down(board, (x,y))
                            return True

            else: # si on est au milieu
                if is_fall(board, (x, y), (x+1, y)):
                    if is_fall(board, (x, y), (x, y+1)):
                        path_right_up(board, (x, y))
                        return True
                    elif is_fall(board, (x, y), (x, y-1)):
                        path_up_left(board, (x, y))
                        return True
                    elif board.M[x][y-1] ==  board.M[x][y+1] and is_point(board, (x,y-1)) and is_point(board, (x,y+1)):
                        board.M[x][y] = board.M[x][y-1]
                        board.points.remove((x, y+1))
                        board.points.remove((x, y-1))
                        board.len_points -= 2
                        return True
                    elif board.M[x-1][y] != "" and not is_no_color(board, (x-1,y)):
                        if board.M[x][y+1] != "" and not is_no_color(board, (x,y+1)):
                            if board.M[x][y+1] == board.M[x-1][y]:
                                path_right_up(board, (x,y))
                                return True
                            else:
                                path_left(board, (x,y))
                                return True
                        elif board.M[x][y-1] != "" and not is_no_color(board, (x,y-1)):
                            if board.M[x][y-1] == board.M[x-1][y]:
                                path_up_left(board, (x,y))
                                return True
                            else:
                                path_right(board, (x,y))
                                return True

                elif is_fall(board, (x, y), (x-1, y)):
                    if is_fall(board, (x, y), (x, y+1)):
                        path_down_right(board, (x, y))
                        return True
                    elif is_fall(board, (x, y), (x, y-1)):
                        path_left_down(board, (x, y))
                        return True
                    elif board.M[x][y-1] ==  board.M[x][y+1] and is_point(board, (x,y-1)) and is_point(board, (x,y+1)):
                        board.M[x][y] = board.M[x][y-1]
                        board.points.remove((x, y+1))
                        board.points.remove((x, y-1))
                        board.len_points -= 2
                        return True
                    elif board.M[x+1][y] != "" and not is_no_color(board, (x+1,y)):
                        if board.M[x][y+1] != "" and not is_no_color(board, (x,y+1)):
                            if board.M[x][y+1] == board.M[x+1][y]:
                                path_down_right(board, (x,y))
                                return True
                            else:
                                path_left(board, (x,y))
                                return True
                        elif board.M[x][y-1] != "" and not is_no_color(board, (x,y-1)):
                            if board.M[x][y-1] == board.M[x+1][y]:
                                path_left_down(board, (x,y))
                                return True
                            else:
                                path_right(board, (x,y))
                                return True
                
                elif is_fall(board, (x, y), (x, y-1)):
                    if board.M[x-1][y] ==  board.M[x+1][y] and is_point(board, (x-1,y)) and is_point(board, (x+1,y)):
                        board.M[x][y] = board.M[x-1][y]
                        board.points.remove((x+1, y))
                        board.points.remove((x-1, y))
                        board.len_points -= 2
                        return True
                    if board.M[x][y+1] != "" and not is_no_color(board, (x,y+1)):
                        if board.M[x+1][y] != "" and not is_no_color(board, (x+1,y)):
                            if board.M[x][y+1] == board.M[x+1][y]:
                                path_down_right(board, (x,y))
                                return True
                            else:
                                path_up(board, (x,y))
                                return True
                        elif board.M[x-1][y] != "" and not is_no_color(board, (x-1,y)):
                            if board.M[x][y+1] == board.M[x-1][y]:
                                path_right_up(board, (x,y))
                                return True
                            else:
                                path_down(board, (x,y))
                                return True

                elif is_fall(board, (x, y), (x, y+1)):
                    if board.M[x-1][y] ==  board.M[x+1][y] and is_point(board, (x-1,y)) and is_point(board, (x+1,y)):
                        board.M[x][y] = board.M[x-1][y]
                        board.points.remove((x+1, y))
                        board.points.remove((x-1, y))
                        board.len_points -= 2
                        return True
                    if board.M[x][y-1] != "" and not is_no_color(board, (x,y-1)):
                        if board.M[x+1][y] != "" and not is_no_color(board, (x+1,y)):
                            if board.M[x][y-1] == board.M[x+1][y]:
                                path_left_down(board, (x,y))
                                return True
                            else:
                                path_up(board, (x,y))
                                return True
                        elif board.M[x-1][y] != "" and not is_no_color(board, (x-1,y)):
                            if board.M[x][y-1] == board.M[x-1][y]:
                                path_right_up(board, (x,y))
                                return True
                            else:
                                path_down(board, (x,y))
                                return True
    return False

def create_all_path(board):
    is_change = False
    for x in range(board.size):
        for y in range(board.size):
            if creation_path(board, (x, y)):
                is_change = True
    return is_change
