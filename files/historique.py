


def update_execution_time(sheet, size, level, exe_time,cpt):

    # Calculer les coordonnées de la cellule de temps d'exécution en fonction de la taille et du niveau
    col = 3 + level
    row = 4 * (size - 4)
    # print((col,row))
    if type(exe_time) == str :
        sheet.update_cell(row, col,exe_time)
    else:    
        # Mettre à jour la cellule de temps d'exécution avec le nouveau temps
        sheet.update_cell(row, col, round(float(exe_time),5))
    sheet.update_cell(row + 1, col, cpt)


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

        

        connections_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)

        draw_data = DrawData(screen, connections_surface, margin_x, margin_y, cell_width, cell_height)

        

        thread_bf = threading.Thread(target=brut_force,args=(2,2,draw_data))

        thread_bf.start()


        # # Effacer la surface des points
        # points_surface.fill((0, 0, 0, 0))

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


def draw_lines(image_path):
    # Charger l'image
    image = cv2.imread(image_path)

    # Appliquer une opération de détection de contours
    edges = cv2.Canny(image, 50, 150, apertureSize=3)

    # Appliquer une transformée de Hough pour détecter les lignes
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

    # Dessiner les lignes détectées sur l'image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Enregistrer l'image avec les lignes détectées
    output_path = "lines_detected_v2.png"
    cv2.imwrite(output_path, image)

def extract_red_board(image_path):
    # Charger l'image avec les lignes rouges
    image_lines = cv2.imread(image_path)

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image_lines, cv2.COLOR_BGR2GRAY)

    # Appliquer un seuillage adaptatif pour binariser l'image
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Trouver les contours des cases
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Trouver le contour le plus grand (le plateau de Flow Free)
    largest_contour = max(contours, key=cv2.contourArea)

    # Créer un masque vide de la même taille que l'image originale
    mask = np.zeros_like(image_lines)

    # Dessiner le contour du plateau sur le masque en blanc (255)
    cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Appliquer le masque sur l'image originale pour extraire le plateau de jeu
    extracted_board = cv2.bitwise_and(image_lines, mask)

    # Enregistrer l'image extraite du plateau
    output_path = "extracted_board.png"
    cv2.imwrite(output_path, extracted_board)

    return output_path

def brut_force_with_draw(self, x, y,draw_data):
    print("test 1 ")
    # Efface la surface des connexions en la remplissant avec une couleur de fond transparente
    draw_data.connections_surface.fill((0, 0, 0, 0))

    # Dessine les nouvelles connexions sur la surface des connexions
    self.draw_connections(draw_data.connections_surface, draw_data.margin_x, draw_data.margin_y, draw_data.cell_width, draw_data.cell_height)

    # Blitte la surface des connexions sur l'écran principal
    draw_data.screen.blit(draw_data.connections_surface, (0, 0))

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


def detect_horizontal_lines(image_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer une opération de détection de contours
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Appliquer une transformée de Hough pour détecter les lignes
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

    # Calculer les tailles des lignes
    line_lengths = [abs(line[0][3] - line[0][1]) for line in lines]

    # Afficher la taille de tous les traits
    print("Taille des traits avant le filtrage:")
    for length in line_lengths:
        print(length)

    # Trouver les tailles les plus fréquentes
    line_lengths_counts = Counter(line_lengths)
    most_common_lengths = line_lengths_counts.most_common()

    # Trouver la taille la plus fréquente à 2 près
    most_common_length = max(most_common_lengths, key=lambda x: x[1])[0]

    # Filtrer les lignes en conservant uniquement celles ayant la taille la plus fréquente à 2 près
    filtered_lines = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        line_length = abs(y2 - y1)
        if line_length != 0 and abs(line_length - most_common_length) <= 2:
            filtered_lines.append(line)

    # Surligner les lignes filtrées sur l'image
    for line in filtered_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Enregistrer l'image avec les lignes filtrées
    cv2.imwrite(output_path, image)

    # Trouver le trait le plus à droite
    rightmost_line = sorted(filtered_lines, key=lambda line: max(line[0][0], line[0][2]))[-1]

    # Trouver le trait le plus à gauche
    leftmost_line = sorted(filtered_lines, key=lambda line: min(line[0][0], line[0][2]))[0]

    # Récupérer les coordonnées des extrémités des traits les plus haut et les plus bas
    top_left = (leftmost_line[0][0], min(leftmost_line[0][1], leftmost_line[0][3]))
    top_right = (rightmost_line[0][2], min(rightmost_line[0][1], rightmost_line[0][3]))
    bottom_left = (leftmost_line[0][0], max(leftmost_line[0][1], leftmost_line[0][3]))
    bottom_right = (rightmost_line[0][2], max(rightmost_line[0][1], rightmost_line[0][3]))

    # Afficher les coordonnées des 4 sommets
    print("Top Left: ", top_left)
    print("Top Right: ", top_right)
    print("Bottom Left: ", bottom_left)
    print("Bottom Right: ", bottom_right)

    # Retourner les coordonnées des 4 sommets
    return top_left, top_right, bottom_left, bottom_right