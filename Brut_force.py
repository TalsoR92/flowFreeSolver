from Board import Board

class BrutForce(Board):

    def all_dots_path(self):
        list_all_path = []
        
        for color in self.pos_points:
            list_all_path.append(self.dots_path(color[0]))


    def dots_path(self, positions):
            start_pos = positions[0]
            visited = set()
            paths = []

            def dfs(current_pos, color, path):
                visited.add(current_pos)
                path.append(current_pos)

                if current_pos == end_pos:
                    paths.append(path[:])
                else:
                    valid, neighbors = self.available_cases_for_dfs(current_pos, color, visited)
                    if valid:
                        for neighbor in neighbors:
                            dfs(neighbor, color, path)

                path.pop()
                visited.remove(current_pos)

            color = self.board[start_pos.y][start_pos.x].color
            dfs(start_pos, color, [])

            return paths

    
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


    def brut_force_with_draw(self, x, y,draw_data):
        print("test 1 ")

        # Dessine les nouvelles connexions sur la surface des connexions
        self.draw_connections(draw_data.connections_surface_copy, draw_data.margin_x, draw_data.margin_y, draw_data.cell_width, draw_data.cell_height)

        # Blitte la surface des connexions sur l'écran principal
        draw_data.screen.blit(draw_data.connections_surface_copy, (0, 0))

        # Rafraîchit l'affichage
        pygame.display.flip()


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
                if self.brut_force_with_draw(self.pos_points[c[index + 1]][0].x, self.pos_points[c[index + 1]][0].y,draw_data):
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

                    if self.brut_force_with_draw(pos.x, pos.y,draw_data):
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

                    if self.brut_force_with_draw(pos.x, pos.y,draw_data):
                        return True
                    else:
                        self.board[y][x].next_case = None

                        self.board[pos.y][pos.x] = None
                return False   


    def check_color_line_adjacent(self, pos, new_pos, color):
        if pos.x != new_pos.x - 1 and new_pos.x - 1 >= 0:
            if self.board[new_pos.y][new_pos.x - 1] is not None:
                if self.board[new_pos.y][new_pos.x - 1].color == color and (isinstance(self.board[new_pos.y][new_pos.x - 1], Colored) or self.board[new_pos.y][new_pos.x - 1].connected):
                    return True

        if pos.y != new_pos.y - 1 and new_pos.y - 1 >= 0:
            if self.board[new_pos.y - 1][new_pos.x] is not None:
                if self.board[new_pos.y - 1][new_pos.x].color == color and (isinstance(self.board[new_pos.y - 1][new_pos.x], Colored) or self.board[new_pos.y - 1][new_pos.x].connected):
                    return True

        if pos.x != new_pos.x + 1 and new_pos.x + 1 < self.width:
            if self.board[new_pos.y][new_pos.x + 1] is not None:
                if self.board[new_pos.y][new_pos.x + 1].color == color and (isinstance(self.board[new_pos.y][new_pos.x + 1], Colored)or self.board[new_pos.y][new_pos.x + 1].connected):
                    return True

        if pos.y != new_pos.y + 1 and new_pos.y + 1  < self.height:
            if self.board[new_pos.y + 1][new_pos.x] is not None:
                if self.board[new_pos.y + 1][new_pos.x].color == color and (isinstance(self.board[new_pos.y + 1][new_pos.x], Colored) or self.board[new_pos.y + 1][new_pos.x].connected):
                    return True

        return False


    def available_cases(self, pos, color):
        neighbors = []

        if pos.x-1 >= 0:
            if self.board[pos.y][pos.x-1] is None:
                neighbors.append(Position(pos.x-1, pos.y))
            elif isinstance(self.board[pos.y][pos.x-1], Point) and self.board[pos.y][pos.x-1].color == color and not self.board[pos.y][pos.x-1].connected:
                return (True, [Position(pos.x-1, pos.y)])

        if pos.y-1 >= 0:
            if self.board[pos.y-1][pos.x] is None:
                neighbors.append(Position(pos.x, pos.y-1))
            elif isinstance(self.board[pos.y-1][pos.x], Point) and self.board[pos.y-1][pos.x].color == color and not self.board[pos.y-1][pos.x].connected:
                return (True, [Position(pos.x, pos.y-1)])

        if pos.x+1 < self.width:
            if self.board[pos.y][pos.x+1] is None:
                neighbors.append(Position(pos.x+1, pos.y))
            elif isinstance(self.board[pos.y][pos.x+1], Point) and self.board[pos.y][pos.x+1].color == color and not self.board[pos.y][pos.x+1].connected:
                return (True, [Position(pos.x+1, pos.y)])

        if pos.y+1 < self.height:
            if self.board[pos.y+1][pos.x] is None:
                neighbors.append(Position(pos.x, pos.y+1))
            elif isinstance(self.board[pos.y+1][pos.x], Point) and self.board[pos.y+1][pos.x].color == color and not self.board[pos.y+1][pos.x].connected:
                return (True, [Position(pos.x, pos.y+1)])

        return (False, neighbors)

    def available_cases_for_dfs(self, pos, color,visited):
        neighbors = []
        if pos.x-1 >= 0 and Position(pos.x-1,pos.y) not in visited:
            if self.board[pos.y][pos.x-1] is None:
                neighbors.append(Position(pos.x-1, pos.y))
            elif isinstance(self.board[pos.y][pos.x-1], Point) and self.board[pos.y][pos.x-1].color == color and not self.board[pos.y][pos.x-1].connected:
                return (True, [Position(pos.x-1, pos.y)])

        if pos.y-1 >= 0 and Position(pos.x,pos.y-1) not in visited:
            if self.board[pos.y-1][pos.x] is None:
                neighbors.append(Position(pos.x, pos.y-1))
            elif isinstance(self.board[pos.y-1][pos.x], Point) and self.board[pos.y-1][pos.x].color == color and not self.board[pos.y-1][pos.x].connected:
                return (True, [Position(pos.x, pos.y-1)])

        if pos.x+1 < self.width and Position(pos.x+1,pos.y) not in visited:
            if self.board[pos.y][pos.x+1] is None:
                neighbors.append(Position(pos.x+1, pos.y))
            elif isinstance(self.board[pos.y][pos.x+1], Point) and self.board[pos.y][pos.x+1].color == color and not self.board[pos.y][pos.x+1].connected:
                return (True, [Position(pos.x+1, pos.y)])

        if pos.y+1 < self.height and Position(pos.x,pos.y+1) not in visited:
            if self.board[pos.y+1][pos.x] is None:
                neighbors.append(Position(pos.x, pos.y+1))
            elif isinstance(self.board[pos.y+1][pos.x], Point) and self.board[pos.y+1][pos.x].color == color and not self.board[pos.y+1][pos.x].connected:
                return (True, [Position(pos.x, pos.y+1)])

        return (False, neighbors)

    def check_all_points_accessible(self,position, color):
        keys = list(self.pos_points)
        first = keys.index(color)

        # check si la paire en cours de recherche est rejoignable
        if not self.dfs_points_accessible(position,color,[]):
            return False

        # check si les paires suivant la paire en recherche sont rejoignable
        for i in range(first+1,self.nb_color):
            if not self.dfs_points_accessible(self.pos_points[keys[i]][0],keys[i],[]):
                return False

        return True


    def dfs_points_accessible(self, position, color, visited):

        # Marquer la position comme visitée
        visited.append(position)

        (test, neighbors) = self.available_cases_for_dfs(position, color, visited)

        if test:
            return True
        
        for pos in neighbors:
            if self.dfs_points_accessible(pos, color, visited):
                return True

        return False

