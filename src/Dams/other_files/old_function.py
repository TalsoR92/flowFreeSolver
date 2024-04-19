# from dfs_v2.py
def neighboring_available_cases_with_filling(board, pos, color):
    """
    Optimization:
        This function have stupid filling (REMPLISSAGE).

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

    if pos.x-1 >= 0:
        if board.board[pos.y][pos.x-1] is None:
            neighbors.append(Position(pos.x-1, pos.y))
        elif isinstance(board.board[pos.y][pos.x-1], Point) and board.board[pos.y][pos.x-1].color == color and not board.board[pos.y][pos.x-1].connected:
            return (True, [Position(pos.x-1, pos.y)])

    if pos.y-1 >= 0:
        if board.board[pos.y-1][pos.x] is None:
            neighbors.append(Position(pos.x, pos.y-1))
        elif isinstance(board.board[pos.y-1][pos.x], Point) and board.board[pos.y-1][pos.x].color == color and not board.board[pos.y-1][pos.x].connected:
            return (True, [Position(pos.x, pos.y-1)])

    if pos.x+1 < board.width:
        if board.board[pos.y][pos.x+1] is None:
            neighbors.append(Position(pos.x+1, pos.y))
        elif isinstance(board.board[pos.y][pos.x+1], Point) and board.board[pos.y][pos.x+1].color == color and not board.board[pos.y][pos.x+1].connected:
            return (True, [Position(pos.x+1, pos.y)])

    if pos.y+1 < board.height:
        if board.board[pos.y+1][pos.x] is None:
            neighbors.append(Position(pos.x, pos.y+1))
        elif isinstance(board.board[pos.y+1][pos.x], Point) and board.board[pos.y+1][pos.x].color == color and not board.board[pos.y+1][pos.x].connected:
            return (True, [Position(pos.x, pos.y+1)])

    return (False, neighbors)




def brut_force(self, x, y):

        if isinstance(self.board[y][x], Colored) and self.check_color_line_adjacent(self.board[y][x].prev_case, Position(x,y), self.board[y][x].color):
            return False
        if not self.check_all_points_accessible(Position(x,y), self.board[y][x].color):
            return False

        (test, L) = self.available_cases(Position(x, y), self.board[y][x].color)

        # print(self.board[y][x].color)
        # print(self)

        # la prochaine position est la paire
        if test:
            c = list(self.pos_points.keys())
            index = c.index(self.board[y][x].color)
            if index + 1 < self.nb_color:

                new_x = L[0].x
                new_y = L[0].y
                self.board[new_y][new_x].neighbour = Position(x, y)
                self.board[new_y][new_x].connected = True
                self.board[new_y][new_x].pair = True

                self.board[y][x].next_case = L[0]
                if self.brut_force(self.pos_points[c[index + 1]][0].x, self.pos_points[c[index + 1]][0].y):
                    return True
                else:
                    self.board[new_y][new_x].neighbour = None
                    self.board[new_y][new_x].connected = False
                    self.board[new_y][new_x].pair = False

                    self.board[y][x].next_case = None

                    return False
            else:
                if self.check_win():
                    new_x = L[0].x
                    new_y = L[0].y
                    self.board[new_y][new_x].neighbour = Position(x, y)
                    self.board[new_y][new_x].connected = True
                    self.board[new_y][new_x].pair = True

                    self.board[y][x].next_case = L[0]
                    return True
                return False
        # il n'y a plus de case disponible
        elif L == []:
            return False
        else:
            # la case de départ est le point de départ
            if isinstance(self.board[y][x], Point):
                for pos in L:
                    self.board[y][x].neighbor = pos
                    self.board[y][x].connected = True

                    self.board[pos.y][pos.x] = Colored(Position(x, y), None, self.board[y][x].color)

                    if self.brut_force(pos.x, pos.y):
                        return True
                    else:
                        self.board[y][x].neighbor = None
                        self.board[y][x].connected = False

                        self.board[pos.y][pos.x] = None

                return False
            # autre cas
            else:
                for pos in L:
                    self.board[y][x].next_case = pos

                    self.board[pos.y][pos.x] = Colored(Position(x, y),None,self.board[y][x].color)

                    if self.brut_force(pos.x, pos.y):
                        return True
                    else:
                        self.board[y][x].next_case = None

                        self.board[pos.y][pos.x] = None
                return False