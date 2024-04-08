from Dams.include import *
from Dams.class_files.Position import *
from Dams.class_files.Colored import *
from Dams.class_files.Point import *

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None for _ in range(width)] for _ in range(height)]

        self.pos_points = {} # {"bleu":(pos,pos), "red":(pos,pos)}
        self.nb_color = 0

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
    

    def create_class_board(self,flow_matrix):
        '''
        Create the class board using the given flow matrix.

        Args:
        - flow_matrix (List[List[str]]): The matrix representing the game board obtained from the JSON file of levels.
        '''
        self.make_pos_points(flow_matrix)
        self.create_board_from_matrix(flow_matrix)

    # créer la map de position des points dans un object Board depuis la matrice du json
    def make_pos_points(self, M):
        '''
        Goal: To construct the positions of pairs of color points as a map for the game board.

        Args:
        - M (List[List[str]]): The matrix representing the game board obtained from the JSON file of levels.
        '''
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

    # créer un object Board depuis la matrice du json
    def create_board_from_matrix(self, flow_matrix):
        '''
        Set up the board by placing colored points on it.

        Args:
        - flow_matrix (List[List[str]]): The matrix representing the game board obtained from the JSON file of levels.
        '''
        for i in range(self.height):
            for j in range(self.width):
                color = flow_matrix[i][j]

                if color:
                    position = Position(j, i)
                    point = Point(position, color)
                    self.board[i][j] = point