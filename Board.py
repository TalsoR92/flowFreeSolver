from files.include import *


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None for _ in range(width)] for _ in range(height)]

        self.pos_points = {}
        self.nb_color = 0

    def draw(self):
        self.board.draw()

    def __str__(self):
        board_str = ""
        for row in self.board:
            row_str = ""
            for cell in row:
                if cell is None:
                    row_str += " -"
                else:
                    if isinstance(cell, Point):
                        color = cell.color[0].upper()
                    elif isinstance(cell, Colored):
                        color = cell.color[0].lower()
                    else:
                        color = "-"
                    row_str += " " + color
            board_str += row_str + "\n"
        return board_str


    def add_point_pair(self, point1,point2):
        self.board[point1.pos.y][point1.pos.x] = point1
        self.board[point2.pos.y][point2.pos.x] = point2
        self.nb_color += 1
        if point1.color in self.pos_points:
            print("Color problem")
            sys.exit()
        self.pos_points[point1.color] = (point1.pos, point2.pos)

    def check_win(self):
        for L in self.board:
            for e in L:
                if e == None:
                    return False
        return True

    def is_empty(self, x, y):
        return self.board[y][x] is None


    def draw(self):
        # Initialisation de Pygame
        pygame.init()

        # Création de la fenêtre
        size_x = 800
        size_y = 800
        window_size = (size_x, size_y)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Flow Free Board")

        # Dimensions de chaque case du plateau
        cell_width = size_x // max(self.width, self.height) * 0.8
        cell_height = size_x // max(self.width, self.height) * 0.8

        # Dimensions du contour de chaque case
        border_width = 1

        # Calcul des marges pour centrer la board
        margin_x = (size_x - self.width * cell_width) // 2
        margin_y = (size_y - self.height * cell_height) // 2

        # Remplit l'écran principal avec la couleur de fond (blanc)
        screen.fill((255, 255, 255))

        # Initialise la board avec les cases vides et récupère la liste des boutons
        buttons = self.initialize_board(screen, margin_x, margin_y, cell_width, cell_height, border_width)


        # Crée une surface avec une transparence totale pour les points
        points_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)

        # Dessiner les points sur la surface des points
        self.initialize_points(points_surface, margin_x, margin_y, cell_width, cell_height)

        # Copier la surface des points sur l'écran principal
        screen.blit(points_surface, (0, 0))

        # Rafraîchir l'affichage
        pygame.display.flip()

        self.draw_connections(screen, margin_x, margin_y, cell_width, cell_height)
        
        # Rafraîchir l'affichage
        pygame.display.flip()

        # Boucle principale du jeu
        running = True
        while running:

            events = pygame.event.get()  # Récupère les événements à chaque itération

            # Fermer la fênetre quit button cliqué
            if self.check_quit_button_click(events):
                break

            clicked_buttons = self.check_click(buttons,events)

            # if clicked_buttons != []:
            #     print(clicked_buttons)           

        # Fermeture de Pygame
        pygame.quit()

    def draw_test(self):
         # Initialisation de Pygame
        pygame.init()

        # Création de la fenêtre
        size_x = 800
        size_y = 800
        window_size = (size_x, size_y)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Flow Free Board")

        # Dimensions de chaque case du plateau
        cell_width = size_x // max(self.width, self.height) * 0.8
        cell_height = size_x // max(self.width, self.height) * 0.8

        # Dimensions du contour de chaque case
        border_width = 1

        # Calcul des marges pour centrer la board
        margin_x = (size_x - self.width * cell_width) // 2
        margin_y = (size_y - self.height * cell_height) // 2

        # Remplit l'écran principal avec la couleur de fond (blanc)
        screen.fill((255, 255, 255))

        # Initialise la board avec les cases vides et récupère la liste des boutons
        buttons = self.initialize_board(screen, margin_x, margin_y, cell_width, cell_height, border_width)

        # Crée une surface pour le carré
        square_surface = pygame.Surface((size_x // 2, size_y // 2))
        square_surface.fill((0, 0, 255))  # Carré bleu

        # Dessine le carré sur la surface
        pygame.draw.rect(square_surface, (0, 0, 255), pygame.Rect(0, 0, size_x // 2, size_y // 2))

        # Copie la surface du carré sur l'écran principal
        screen.blit(square_surface, (size_x // 4, size_y // 4))

        # Rafraîchit l'affichage
        pygame.display.flip()

        # Attend 5 secondes
        time.sleep(5)

        # Efface le carré en remplissant la surface avec la couleur de fond
        square_surface.fill((255, 255, 255))

        # Rafraîchit l'affichage pour effacer le carré affiché précédemment
        pygame.display.flip()

        # Boucle principale du jeu
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Quitter Pygame
        pygame.quit()

    def draw_with_brut_force(self):
        # Initialisation de Pygame
        pygame.init()

        # Création de la fenêtre
        size_x = 800
        size_y = 800
        window_size = (size_x, size_y)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Flow Free Board")

        # Dimensions de chaque case du plateau
        cell_width = size_x // max(self.width, self.height) * 0.8
        cell_height = size_x // max(self.width, self.height) * 0.8

        # Dimensions du contour de chaque case
        border_width = 1

        # Calcul des marges pour centrer la board
        margin_x = (size_x - self.width * cell_width) // 2
        margin_y = (size_y - self.height * cell_height) // 2

        # Remplit l'écran principal avec la couleur de fond (blanc)
        screen.fill((255, 255, 255))

        # Initialise la board avec les cases vides et récupère la liste des boutons
        buttons = self.initialize_board(screen, margin_x, margin_y, cell_width, cell_height, border_width)


        # Crée une surface avec une transparence totale pour les points
        points_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)

        # Dessiner les points sur la surface des points
        self.initialize_points(points_surface, margin_x, margin_y, cell_width, cell_height)

        # Copier la surface des points sur l'écran principal
        screen.blit(points_surface, (0, 0))



        # Crée une surface avec une transparence totale pour les connexions
        connections_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)

        
        draw_data = DrawData(screen, connections_surface, margin_x, margin_y, cell_width, cell_height)

        thread_bf = threading.Thread(target=self.brut_force_with_draw,args=(2,2,draw_data))

        thread_bf.start()


        # Boucle principale du jeu
        running = True
        while running:

            events = pygame.event.get()  # Récupère les événements à chaque itération

            # Fermer la fênetre quit button cliqué
            if self.check_quit_button_click(events):
                break

            clicked_buttons = self.check_click(buttons,events)

            # if clicked_buttons != []:
            #     print(clicked_buttons)           

        # Fermeture de Pygame
        pygame.quit()
    # Fonction pour dessiner les points de la board
    def initialize_points(self, screen, margin_x, margin_y, cell_width, cell_height):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.board[y][x]
                if isinstance(cell, Point):
                    point_size = min(cell_width, cell_height) * 1.5 // 4
                    point_pos = (
                        margin_x + x * cell_width + cell_width // 2,
                        margin_y + y * cell_height + cell_height // 2
                    )
                    # print(cell)
                    # print(cell.color)
                    pygame.draw.circle(screen, cell.color, point_pos, point_size)

    def draw_connections(self, screen, margin_x, margin_y, cell_width, cell_height):
        line_width = round(min(cell_width, cell_height) // 5)

        for y in range(self.height):
            for x in range(self.width):
                if isinstance(self.board[y][x], Colored):
                    color = self.board[y][x].color

                    if self.board[y][x].prev_case:
                        start_pos = (margin_x + x * cell_width + cell_width // 2, margin_y + y * cell_height + cell_height // 2)
                        prev_pos = self.board[y][x].prev_case
                        end_pos = (margin_x + prev_pos.x * cell_width + cell_width // 2, margin_y + prev_pos.y * cell_height + cell_height // 2)
                        pygame.draw.line(screen, color, start_pos, end_pos, line_width)

                    if self.board[y][x].next_case:
                        start_pos = (margin_x + x * cell_width + cell_width // 2, margin_y + y * cell_height + cell_height // 2)
                        next_pos = self.board[y][x].next_case
                        end_pos = (margin_x + next_pos.x * cell_width + cell_width // 2, margin_y + next_pos.y * cell_height + cell_height // 2)
                        pygame.draw.line(screen, color, start_pos, end_pos, line_width)

    def initialize_board(self, screen, margin_x, margin_y, cell_width, cell_height, border_width):
        # Dessine les cases vides
        buttons = []  # Liste pour stocker les boutons
        for y in range(self.height):
            for x in range(self.width):
                cell = self.board[y][x]
                rect = pygame.Rect(
                    margin_x + x * cell_width, margin_y + y * cell_height,
                    cell_width, cell_height
                )
                button = Button(rect, cell)  # Crée un bouton avec le rectangle et la cellule
                buttons.append(button)  # Ajoute le bouton à la liste
                pygame.draw.rect(screen, (0, 0, 0), rect, border_width)

        return buttons  # Retourne la liste des boutons

    def check_quit_button_click(self,events):

        for event in events:
            if event.type == pygame.QUIT:
                return True
        return False
                
    def check_click(self, buttons,events):
        clicked_buttons = []

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Vérifie le clic gauche de la souris
                mouse_pos = pygame.mouse.get_pos()
                print("ouiii")

                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        clicked_buttons.append(button)

        return clicked_buttons




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

    def check_case_access_blockage(self,x,y):

        if x-1 >= 0 :
            if self.board[y][x-1] != None and self.board[y][x-1].color != self.board[y][x].color:
                return True
            if y-1 >= 0 and self.board[y-1][x-1] != None and self.board[y-1][x-1].color != self.board[y][x].color:
                return True
            if y+1 < self.height and self.board[y+1][x-1] != None and self.board[y+1][x-1].color != self.board[y][x].color:
                return True
        
        if x+1 < self.width:
            if self.board[y][x+1] != None and self.board[y][x+1].color != self.board[y][x].color:
                return True
            if y+1 < self.height and self.board[y+1][x+1] != None and self.board[y+1][x+1].color != self.board[y][x].color:
                return True
            if y-1 >= 0 and self.board[y-1][x+1] != None and self.board[y-1][x+1].color != self.board[y][x].color:
                return True


        if y-1 >= 0 and self.board[y-1][x] != None and self.board[y-1][x].color != self.board[y][x].color:
            return True
        if y+1 < self.height and self.board[y+1][x] != None and self.board[y+1][x].color != self.board[y][x].color:
            return True 
        
        return False

    def brut_force_main(self):
        global cpt
        global cpt_ccla
        global cpt_capa
        global cpt_ccla_tot
        global cpt_capa_tot

        global time_ccla
        global time_capa

        cpt = 0
        cpt_ccla = 0
        cpt_ccla_tot = 0
        cpt_capa = 0
        cpt_capa_tot = 0
        time_ccla = 0
        time_capa = 0

        first_color = next(iter(self.pos_points.values()))[0]

        global exe_start_time
        exe_start_time = time.time()

        try:
            if self.brut_force(first_color.x,first_color.y):
                ratio_ccla = round(cpt_ccla/cpt_ccla_tot*100,2)
                ratio_capa = round(cpt_capa/cpt_capa_tot*100,2)
                print(f"cpt = {cpt}")
                return 1, cpt, ratio_ccla, ratio_capa, time_ccla, time_capa
            ratio_ccla = round(cpt_ccla/cpt_ccla_tot*100,2)
            ratio_capa = round(cpt_capa/cpt_capa_tot*100,2)
            return 0, cpt, ratio_ccla, ratio_capa, time_ccla, time_capa
        except TimeoutError:
            ratio_ccla = round(cpt_ccla/cpt_ccla_tot*100,2)
            ratio_capa = round(cpt_capa/cpt_capa_tot*100,2)
            return -1, cpt, ratio_ccla, ratio_capa, time_ccla, time_capa
        
    def brut_force(self, x, y):
        # print()
        # print(self)
        global cpt
        cpt += 1
        global exe_start_time
        if time.time() - exe_start_time > 30:
            raise TimeoutError("time_out")

        if isinstance(self.board[y][x], Colored):
            global time_ccla
            start = time.time()
            global cpt_ccla_tot
            cpt_ccla_tot += 1
            if self.check_color_line_adjacent(self.board[y][x].prev_case, Position(x,y), self.board[y][x].color):
                global cpt_ccla
                cpt_ccla += 1
                # print("ccla")
                time_ccla += time.time() - start
                return False
            time_ccla += time.time() - start
        
        if isinstance(self.board[y][x], Colored) and self.check_case_access_blockage(x,y):
            global time_capa
            start = time.time()
            global cpt_capa_tot
            cpt_capa_tot += 1
            if not self.check_all_points_accessible(Position(x,y), self.board[y][x].color):
                # print(self)
                # print("capa")
                global cpt_capa
                cpt_capa += 1
                time_capa += time.time() - start
                return False
            time_capa += time.time() - start

        # if isinstance(self.board[y][x], Colored) and self.check_case_access_blockage(x,y) and not self.check_all_points_accessible(Position(x,y), self.board[y][x].color):
        #     return False

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

        # # Dessine les nouvelles connexions sur la surface des connexions
        # self.draw_connections(draw_data.connections_surface_copy, draw_data.margin_x, draw_data.margin_y, draw_data.cell_width, draw_data.cell_height)

        # # Blitte la surface des connexions sur l'écran principal
        # draw_data.screen.blit(draw_data.connections_surface_copy, (0, 0))

        # # Rafraîchit l'affichage
        # pygame.display.flip()


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



    def create_class_board(self,flow_matrix):
        self.make_pos_points(flow_matrix)
        self.create_board_from_matrix(flow_matrix)

    def make_pos_points(self, M):
        list_color = []
        for y in range(len(M)):
            for x in range(len(M[y])):
                color = M[y][x]
                if color != "":
                    if color not in self.pos_points:
                        self.pos_points[color] = (Position(x, y), None)
                    else:
                        if self.pos_points[color][1] is not None:
                            raise ValueError("Erreur : Deuxième paire d'une même couleur déjà présente")
                        else:
                            self.pos_points[color] = (self.pos_points[color][0], Position(x, y))
                            self.nb_color += 1

    def create_board_from_matrix(self, flow_matrix):
        for i in range(self.height):
            for j in range(self.width):
                color = flow_matrix[i][j]

                if color:
                    position = Position(j, i)
                    point = Point(position, color)
                    self.board[i][j] = point





# board.board[4][1] = Colored(None, None, "red")
# board.board[4][2] = Colored(None, None, "red")
# board.board[5][2] = Colored(None, None, "red")
# board.board[5][1] = Colored(None, None, "red")
# board.board[0][1] = Colored(None, None, "yellow")
# board.board[1][1] = Colored(None, None, "yellow")
# board.board[1][1].attribute = Colored(None, None, "blue")
# board.board[2][1].attribute = Colored(None, None, "green")


# print(board.check_win())
# print(board.pos_points)
# board.draw()
# print(board.board[0][2])

# print(board.check_color_line_adjacent(Position(2,5), Position(1,5), "red"))

# exit(0)

# start = time.time()

# print(board.brut_force(0, 4))
# print("time : "+str(time.time()-start))
# print(board)
# print(board.draw())

# board2 = Board(8,8)

# p1 = Point(Position(2,2),"red")
# p2 = Point(Position(6,4),"red")
# board2.add_point_pair(p1,p2)

# p1 = Point(Position(0,5),"navy")
# p2 = Point(Position(6,1),"navy")
# board2.add_point_pair(p1,p2)

# p1 = Point(Position(2,4),"yellow")
# p2 = Point(Position(5,5),"yellow")
# board2.add_point_pair(p1,p2)

# p1 = Point(Position(1,1),"green")
# p2 = Point(Position(5,4),"green")
# board2.add_point_pair(p1,p2)

# p1 = Point(Position(3,0),"orange")
# p2 = Point(Position(5,3),"orange")
# board2.add_point_pair(p1,p2)

# p1 = Point(Position(4,1),"blue")
# p2 = Point(Position(7,0),"blue")
# board2.add_point_pair(p1,p2)

# p1 = Point(Position(5,1),"pink")
# p2 = Point(Position(6,3),"pink")
# board2.add_point_pair(p1,p2)


# board2.board[4][1] = Colored(None, None, "red")
# board2.board[4][2] = Colored(None, None, "red")
# board2.board[5][2] = Colored(None, None, "red")
# board2.board[5][1] = Colored(None, None, "red")
# board2.board[0][1] = Colored(None, None, "yellow")
# board2.board[1][1] = Colored(None, None, "yellow")

# print(board2)
# start = time.time()

# print(board2.brut_force(2, 2))
# print("time : "+str(time.time()-start))


# print(board2[])

# print(board2.brut_force(2,2))
# print(board2.draw())

# print(board2.draw())