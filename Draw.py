from Board import Board

class Draw(Board):


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
                    print(cell.color)
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

