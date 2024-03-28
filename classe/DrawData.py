class DrawData:
    def __init__(self, screen, connections_surface_copy, margin_x, margin_y, cell_width, cell_height):
        self.screen = screen
        self.connections_surface_copy = connections_surface_copy
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.cell_width = cell_width
        self.cell_height = cell_height
    
    def clear_connections_surface(self):
        self.connections_surface_copy.fill((0, 0, 0, 0))
        
    def __copy__(self):
        # Crée une nouvelle instance de la classe DrawData avec les mêmes attributs
        return DrawData(self.screen, self.connections_surface, self.margin_x, self.margin_y, self.cell_width, self.cell_height)

    '''
   

    '''


    # def draw(self):
    #     # Initialisation de Pygame
    #     pygame.init()

    #     # Création de la fenêtre
    #     size_x = 800
    #     size_y = 800
    #     window_size = (size_x, size_y)
    #     screen = pygame.display.set_mode(window_size)
    #     pygame.display.set_caption("Flow Free Board")

    #     # Dimensions de chaque case du plateau
    #     cell_width = size_x // max(self.width, self.height) * 0.8
    #     cell_height = size_x // max(self.width, self.height) * 0.8

    #     # Dimensions du contour de chaque case
    #     border_width = 1

    #     # Calcul des marges pour centrer la board
    #     margin_x = (size_x - self.width * cell_width) // 2
    #     margin_y = (size_y - self.height * cell_height) // 2

    #     # Remplit l'écran principal avec la couleur de fond (blanc)
    #     screen.fill((255, 255, 255))

    #     # Initialise la board avec les cases vides et récupère la liste des boutons
    #     buttons = self.initialize_board(screen, margin_x, margin_y, cell_width, cell_height, border_width)


    #     # Crée une surface avec une transparence totale pour les points
    #     points_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)

    #     # Dessiner les points sur la surface des points
    #     self.initialize_points(points_surface, margin_x, margin_y, cell_width, cell_height)

    #     # Copier la surface des points sur l'écran principal
    #     screen.blit(points_surface, (0, 0))

    #     # Rafraîchir l'affichage
    #     pygame.display.flip()

        
        

    #     def self.brut_force_with_draw( x, y):
    #         connections_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
    #         print("oooooooooookkkkkkkkkkkkkkkk")
    #         self.draw_connections(connections_surface, margin_x, margin_y, cell_width, cell_height)

    #         screen.blit(connections_surface, (0, 0))

    #         pygame.display.flip()
    #         time.sleep(0.01)
            
    #         if isinstance(self.board[y][x], Colored) and self.check_color_line_adjacent(self.board[y][x].prev_case, Position(x,y), self.board[y][x].color):
    #             return False
    #         if not self.check_all_points_accessible(Position(x,y), self.board[y][x].color):
    #             return False

    #         (test, L) = self.available_cases(Position(x, y), self.board[y][x].color)

    #         # print(self.board[y][x].color)
    #         # print(self)

    #         # la prochaine position est la paire
    #         if test:
    #             c = list(self.pos_points.keys())
    #             index = c.index(self.board[y][x].color)
    #             if index + 1 < self.nb_color:

    #                 new_x = L[0].x
    #                 new_y = L[0].y
    #                 self.board[new_y][new_x].neighbour = Position(x, y)
    #                 self.board[new_y][new_x].connected = True
    #                 self.board[new_y][new_x].pair = True

    #                 self.board[y][x].next_case = L[0]
    #                 if self.brut_force_with_draw(self.pos_points[c[index + 1]][0].x, self.pos_points[c[index + 1]][0].y):
    #                     return True
    #                 else:
    #                     self.board[new_y][new_x].neighbour = None
    #                     self.board[new_y][new_x].connected = False
    #                     self.board[new_y][new_x].pair = False

    #                     self.board[y][x].next_case = None

    #                     return False
    #             else:
    #                 if self.check_win():
    #                     new_x = L[0].x
    #                     new_y = L[0].y
    #                     self.board[new_y][new_x].neighbour = Position(x, y)
    #                     self.board[new_y][new_x].connected = True
    #                     self.board[new_y][new_x].pair = True

    #                     self.board[y][x].next_case = L[0]
    #                     return True
    #                 return False
    #         # il n'y a plus de case disponible
    #         elif L == []:
    #             return False
    #         else:
    #             # la case de départ est le point de départ
    #             if isinstance(self.board[y][x], Point):
    #                 for pos in L:
    #                     self.board[y][x].neighbor = pos
    #                     self.board[y][x].connected = True

    #                     self.board[pos.y][pos.x] = Colored(Position(x, y), None, self.board[y][x].color)

    #                     if self.brut_force_with_draw(pos.x, pos.y):
    #                         return True
    #                     else:
    #                         self.board[y][x].neighbor = None
    #                         self.board[y][x].connected = False

    #                         self.board[pos.y][pos.x] = None

    #                 return False
    #             # autre cas
    #             else:
    #                 for pos in L:
    #                     self.board[y][x].next_case = pos

    #                     self.board[pos.y][pos.x] = Colored(Position(x, y),None,self.board[y][x].color)

    #                     if self.brut_force_with_draw(pos.x, pos.y):
    #                         return True
    #                     else:
    #                         self.board[y][x].next_case = None

    #                         self.board[pos.y][pos.x] = None
    #                 return False    
        

    #     thread_bf = threading.Thread(target=brut_force_with_draw,args=(self,2,2))

    #     thread_bf.start()


    #     # Boucle principale du jeu
    #     running = True
    #     while running:

    #         events = pygame.event.get()  # Récupère les événements à chaque itération

    #         # Fermer la fênetre quit button cliqué
    #         if self.check_quit_button_click(events):
    #             break

    #         clicked_buttons = self.check_click(buttons,events)

    #         # if clicked_buttons != []:
    #         #     print(clicked_buttons)           

    #     # Fermeture de Pygame
    #     pygame.quit()