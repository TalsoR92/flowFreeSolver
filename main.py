
from Board import *
from BF_v2 import *

import os
import json
import numpy as np
import time
from google.oauth2 import service_account
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import OrderedDict

gc = gspread.service_account(filename='google_sheet_api.json')
sh = gc.open_by_key('1CoBJIF6iMFjkIWrz2QNbh1-BcNyCCXjULtsyBwwURVA')
sheet = sh.worksheet('BF ccc posPoints sort dist')


exe_time = 0

def cut_screen_to_json():
    exit(0)
    images_folder = "screen_shot_v3/"
    beginning_file = "board_"
    beginning_output_path = "flow_free_levels/"

    for i in range(5, 10):
        folder_path = "screen_shot_v3/board_" + str(i) + "-" + str(i) + "/"
        output_path_others = "flow_free_levels/levels_for_others/board_" + str(i) + "-" + str(i) + ".json"

        data_python = {}
        data_others = {}

        for j in range(1, 31):
            filename = folder_path + "final_capture_" + str(j) + ".png"

            flow_matrix = generate_flow_matrix(filename, i)
            board = Board(i, i)
            board.create_class_board(flow_matrix)

            data_others["level_" + str(j)] = flow_matrix.tolist()  # Conversion en liste de listes

        with open(output_path_others, "w") as file_others:
            json.dump(data_others, file_others, indent=4)

def timeout_handler(signum, frame):
    raise TimeoutError("Function execution timed out")

def number_to_column_letter(col):
    col_label = ""
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        col_label = chr(65 + remainder) + col_label
    return col_label


def find_cell_coordinates(sheet, nameOfBoardSize, level, name_dataOpti):
    # Récupérer toutes les valeurs de la feuille de calcul
    values = sheet.get_all_values()
    level = str(level)
    # Recherche de la case contenant nameOfBoardSize
    for row_index, row in enumerate(values):
        for col_index, cell_value in enumerate(row):
            if cell_value == nameOfBoardSize:
                
                # Trouver la case avec name_dataOpti en dessous de nameOfBoardSize
                for i in range(row_index + 1, len(values)):
                    if values[i][col_index] == name_dataOpti:
                        # Trouver la case avec level en itérant vers la droite depuis nameOfBoardSize
                        for j in range(col_index + 1, len(row)):
                            if row[j] == level:
                                # Les index de lignes et de colonnes sont basés sur 1 (contrairement aux index 0 dans la programmation)
                                ligne = i + 1
                                colonne = j + 1
                                return (ligne, colonne)

    # Si la valeur n'est pas trouvée, renvoyer None
    return None

def update_google_sheet(sheet, size, level, name_dataOpti, value_dataOpti):
   
    (row,col) = find_cell_coordinates(sheet, f"Level {size}*{size}", level, name_dataOpti)

    if type(value_dataOpti) == str :
        sheet.update_cell(row, col,value_dataOpti)
    else:    
        sheet.update_cell(row, col, round(float(value_dataOpti),6))

# print(find_cell_coordinates(sheet, f"Level {6}*{6}", 5, "cpt"))
# update_google_sheet(sheet, 9, 5, "time_capa", "time_out")
# exit(0)

def pos_point_sort_coord(pos_points):
    # Create a dictionary to store the distances between color pairs
    distances = {}

    # Calculate distances between color pairs
    for color, (pair1, pair2) in pos_points.items():
        distances[color] = abs(pair1.x - pair2.x) + abs(pair1.y - pair2.y)
        print(f"dist of {color} points : {abs(pair1.x - pair2.x) + abs(pair1.y - pair2.y)}")

    # Sort the color pairs in ascending order of distances
    sorted_pairs = OrderedDict(sorted(pos_points.items(), key=lambda x: distances[x[0]]))
    print(list(sorted_pairs.keys()))
    return sorted_pairs


def run_all_level(size_start=5,size_end=9,lvl_start=1,lvl_end=30):

    for size in range(size_start, size_end+1):

        for level in range(lvl_start, lvl_end+1):
            board = Board(size,size)
            # Open the JSON file
            with open("flow_free_levels/levels_for_others/board_" + str(size) + "-" + str(size) + ".json") as file:
                data = json.load(file)

                # Extract the matrix corresponding to the key "level_1"
                flow_matrix = data["level_" + str(level)]
                board.create_class_board(flow_matrix)

            board.pos_points = pos_point_sort_coord(board.pos_points)

            global exe_time
            exe_time = 0

            start = time.time()
            (res, cpt, ratio_ccla, ratio_capa, time_ccla, time_capa) = board.brut_force_main()
            
            exe_time = time.time()-start
            print("Board "+ str(size) + "*" + str(size) + " level "+str(level)+" execution time : ")
            print(exe_time)
            while True:
                try:
                    if res == 1:
                        update_google_sheet(sheet, size, level, "time", exe_time)
                        update_google_sheet(sheet, size, level, "cpt", cpt)

                        update_google_sheet(sheet, size, level, "ratio_ccla", ratio_ccla)
                        update_google_sheet(sheet, size, level, "time_ccla", time_ccla)

                        update_google_sheet(sheet, size, level, "ratio_capa", ratio_capa)
                        update_google_sheet(sheet, size, level, "time_capa", time_capa)
                        
                    elif res == -1:
                        update_google_sheet(sheet, size, level, "time", "time_out")
                        update_google_sheet(sheet, size, level, "cpt", cpt)

                        update_google_sheet(sheet, size, level, "ratio_ccla", ratio_ccla)
                        update_google_sheet(sheet, size, level, "time_ccla", time_ccla)
                        
                        update_google_sheet(sheet, size, level, "ratio_capa", ratio_capa)
                        update_google_sheet(sheet, size, level, "time_capa", time_capa)

                    else:
                        update_google_sheet(sheet, size, level, "time", "!!! impossible !!!")
                        update_google_sheet(sheet, size, level, "cpt", cpt)

                        update_google_sheet(sheet, size, level, "ratio_ccla", ratio_ccla)
                        update_google_sheet(sheet, size, level, "time_ccla", time_ccla)
                        
                        update_google_sheet(sheet, size, level, "ratio_capa", ratio_capa)
                        update_google_sheet(sheet, size, level, "time_capa", time_capa)
                    break

                except Exception as e:
                    print(f"\n\n! Wait to have API capacity !\n\n")
                    time.sleep(5)
            
            print("Board "+ str(size) + "*" + str(size) + " level "+str(level)+" execution time : ")
            print(exe_time)
            print(board)
            print()
            # board.draw()
     
            lvl_start = 1

# run_all_level()

def run_one_level(size_board,nb_level):
    board = Board(size_board,size_board)
    with open(f"flow_free_levels/levels_for_others/board_{size_board}-{size_board}.json") as file:
        data = json.load(file)

        # Extract the matrix corresponding to the key "level_1"
        flow_matrix = data["level_" + str(nb_level)]
        board.create_class_board(flow_matrix)

    pos_point_sort_coord(board.pos_points)

    exe_time = 0

    start = time.time()
    board.brut_force_main()

    exe_time = time.time()-start
    print("Board "+ str(size_board) + "*" + str(size_board) + " level "+str(nb_level)+" execution time : ")
    print(exe_time)
    print()
    board.draw()            

# run_one_level(8, 26)
# run_one_level(8,2)


def run_one_level_v2(size_board,nb_level):
    board = Board(size_board,size_board)
    with open(f"flow_free_levels/levels_for_others/board_{size_board}-{size_board}.json") as file:
        data = json.load(file)

        # Extract the matrix corresponding to the key "level_1"
        flow_matrix = data["level_" + str(nb_level)]
        board.create_class_board(flow_matrix)

    # pos_point_sort_coord(board.pos_points)

    exe_time = 0

    start = time.time()
    dot_all_path(board)

    exe_time = time.time()-start
    print("Board "+ str(size_board) + "*" + str(size_board) + " level "+str(nb_level)+" execution time : ")
    print(exe_time)
    print()
    board.draw()    


run_one_level_v2(5, 1)




def screenShot_to_dfs(screen_shot):
    start = time.time()
    (flow_matrix,nb_x,nb_y) = image_to_flow_matrice(screen_shot, "test.png")
    board = Board(nb_x, nb_y)
    board.create_class_board(flow_matrix)
    print(board)
    print(f"time before brut_force : {round(time.time()-start,3)}")
    board.brut_force_main()
    print(f"time after brut_force : {round(time.time()-start,3)}")
    print(board)
    board.draw()

screen_shot = "IMG_9-9.png"

screen_shot_2 = "IMG_8-10.png"





# screenShot_to_dfs(screen_shot_2)
# exit(0)

# dim = 9
# flow_matrix = generate_flow_matrix(image_path,dim)

# board = Board(dim,dim)

# board.create_class_board(flow_matrix)


# print(board)


# first_color = next(iter(board.pos_points.values()))

# x = first_color[0].x
# y = first_color[0].y

# print(board.brut_force(x,y))
# print(board)

# board.draw()






# from Brut_force import *

# board = Board(5,5)

# p1 = Point(Position(3,0),"red")
# p2 = Point(Position(2,4),"red")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(2,1),"blue")
# p2 = Point(Position(4,3),"blue")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(4,0),"green")
# p2 = Point(Position(3,1),"green")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(1,1),"yellow")
# p2 = Point(Position(4,4),"yellow")
# board.add_point_pair(p1,p2)

# print(board)
# print(board.dots_path("red"))

# print(board.brut_force(3,0))

# print(board.draw())
