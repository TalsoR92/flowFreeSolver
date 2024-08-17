from Toitoine.include import *

class Board:
    def __init__(self, flow_matrix, size_board):
        self.M = [] # matrix de coulleur
        self.size = size_board # taille de la board
        self.nb_color = 0 # nombre de couleur
        self.points = [] # list des point delimitant les path
        self.len_points = 0
        self.no_color = 0 # le numero du path sans couleur

        for i in range(size_board):
            self.M.append([])
            for j in range(size_board):
                self.M[i].append(flow_matrix[i][j])
                if (flow_matrix[i][j] != ""):
                    self.nb_color += 1
                    self.points.append((i, j))
        
        self.len_points = self.nb_color
        self.nb_color //= 2

    '''def solve_board(self):
        solve(self)'''
    
    def dot(self):
        s = ""
        return s
