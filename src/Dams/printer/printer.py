from Dams.class_files.Board import *

def print_all_paths_aligned(positions):
    for sublist_1 in positions:
        for sublist_2 in sublist_1:
            row_str = ""
            for position in sublist_2:
                row_str += f"{position} "
            print(row_str)
            print()  # Ajout d'un saut de ligne après l'impression de chaque sous-liste de positions

        print()
        print()  # Ajout d'un saut de ligne après l'impression de chaque liste de positions
