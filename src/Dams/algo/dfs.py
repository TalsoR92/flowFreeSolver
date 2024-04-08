from Dams.include import *

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