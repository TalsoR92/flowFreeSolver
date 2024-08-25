from Dams.class_files.Board import *
from Dams.class_files.Opti import *
from Dams.printer.printer import *
from Dams.algo.opti_v1 import *
from Dams.include import *
from typing import List, Any, Tuple, Deque, Dict, Optional
from copy import deepcopy

def paths_intersect(path1, path2):
    """
    Check if two paths intersect.
    """
    for pos in path1:
        if pos in path2:
            return True
    return False


def find_valid_combinations(all_paths, nb_paths, current_combo, index, valid_combos):
    """
    Recursively find valid combinations of paths.
    """
    if index == nb_paths:
        valid_combos.append(current_combo.copy())
        return

    for path in all_paths[index]:
        if all(not paths_intersect(path, other_path) for other_path in current_combo):
            current_combo.append(path)
            find_valid_combinations(all_paths, nb_paths, current_combo, index + 1, valid_combos)
            current_combo.pop()

    return valid_combos