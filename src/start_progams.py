import json
import time

# Importez la fonction main depuis le module main.py dans le dossier Dams
from Dams.main import main as main_dams

# Importez la fonction main depuis le module main.py dans le dossier Titi
from Titi.main import main as main_titi

# Importez la fonction main depuis le module main.py dans le dossier Toitoine
from Toitoine.main import main as main_toitoine

def run_all_level(name_dir, size_start=5, size_end=9, lvl_start=1, lvl_end=30):
    tot_exec_times = []

    for size in range(size_start, size_end + 1):
        level_exec_times = []

        for level in range(lvl_start, lvl_end + 1):

            # Open the JSON file
            with open(f"levels_on_json/board_{size}-{size}.json") as file:
                data = json.load(file)

                # Extract the matrix corresponding to the key "level_1"
                flow_matrix = data[f"level_{level}"]

            print(f"Board {size}*{size} level {level}")
            start_time = time.time()

            if name_dir == "Dams":
                main_dams(flow_matrix, size, level)  # Appeler la fonction main de Dams
            elif name_dir == "Titi":
                main_titi(flow_matrix, size)  # Appeler la fonction main de Titi
            elif name_dir == "Toitoine":
                main_toitoine(flow_matrix, size)  # Appeler la fonction main de Toitoine
            else:
                print("Erreur : Nom de répertoire non valide")
                return

            exec_time = time.time() - start_time
            level_exec_times.append(exec_time)

        tot_exec_times.append(level_exec_times)
        lvl_start = 1

    print_stats(name_dir, tot_exec_times, size_start, size_end)


def run_one_level(name_dir, size_board, num_level):
    # Open the JSON file
    with open(f"levels_on_json/board_{size_board}-{size_board}.json") as file:
        data = json.load(file)

        # Extract the matrix corresponding to the specified level
        flow_matrix = data[f"level_{num_level}"]

    start_time = time.time()

    if name_dir == "Dams":
        main_dams(flow_matrix, size_board, num_level)  # Appeler la fonction main de Dams
    elif name_dir == "Titi":
        main_titi(flow_matrix, size_board)  # Appeler la fonction main de Titi
    elif name_dir == "Toitoine":
        main_toitoine(flow_matrix, size_board)  # Appeler la fonction main de Toitoine
    else:
        print("Erreur : Nom de répertoire non valide")
        return

    exec_time = time.time() - start_time


    print(f"Board {size_board}*{size_board} level {num_level} exec time: {exec_time:.6f} secondes\n")
    print()

    return exec_time
        
def print_stats(name, execution_times, size_start=5, size_end=9):
    print(f"Statistic for {name} programs:")
    print("----------------------------------------")
    for i, times in enumerate(execution_times, start=1):
        # Calculer la moyenne
        avg = sum(times) / len(times)

        # Calculer la médiane
        sorted_times = sorted(times)
        n = len(sorted_times)
        if n % 2 == 0:
            median = (sorted_times[n // 2 - 1] + sorted_times[n // 2]) / 2
        else:
            median = sorted_times[n // 2]

        # Calculer le maximum et le minimum
        max_time = max(times)
        min_time = min(times)
        
        # Calculer le temps total
        total_time = sum(times)

        # Afficher les statistiques
        print(f"\nBoard {size_start + i - 1}*{size_start + i - 1}:")
        print(f"Moyenne: {avg:.6f} secondes")
        print(f"Médiane: {median:.6f} secondes")

        print(f"Maximum: {max_time:.6f} secondes")
        print(f"Minimum: {min_time:.6f} secondes\n")
        
        print(f"\nTemps total: {total_time:.6f} secondes\n")
        print("----------------------------------------")


def main():
    # run_all_level("Dams")
    # run_all_level("Dams", 9, 9, 15)
    run_all_level("Dams", 9, 9, 1, 5)
    # run_one_level("Dams", 7, 7)
    # print("\n----------------------------------------\n")
    # run_one_level("Dams", 6, 3)

    # for i in range(1, 3):
    # run_one_level("Dams", 9, 2)
    # return

main()