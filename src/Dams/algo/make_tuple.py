from Dams.include import *

def make_tuple(list_paths: List[List[Any]], size_tuple: int) -> List[Tuple]:
    """
    Return a list of tuples such that for each tuple, each element in `list_paths` has at least one element from the tuple.

    Args:
    - list_paths (List[List[Any]]): The list of paths connecting two color points.
    - size_tuple (int): The maximum size of the searched tuples.

    Goal: To determine the tuples representing mandatory passages in the list of paths connecting two color points.
    """
    if size_tuple == 0 or list_paths == []:
        return []

    def recursive_tuple(m: List[List[Any]], len_m: int, size_tuple: int, actual_tuple: List[Any]) -> None:
        nonlocal tot_tuple
        
        if any(elt in m[0] for elt in actual_tuple):
            if len_m == 1:
                tot_tuple.append(tuple(actual_tuple))
            else:
                recursive_tuple(m[1:], len_m - 1, size_tuple, actual_tuple)
        elif size_tuple > 0:
            if len_m == 1:
                for elt in m[0]:
                    actual_tuple.append(elt)
                    tot_tuple.append(tuple(actual_tuple))
                    actual_tuple.pop()
            else:
                for elt in m[0]:
                    actual_tuple.append(elt)
                    recursive_tuple(m[1:], len_m - 1, size_tuple - 1, actual_tuple)
                    actual_tuple.pop()

    tot_tuple = []
    len_paths = len(list_paths)
    for elt in list_paths[0]:
        recursive_tuple(list_paths[1:], len_paths - 1, size_tuple - 1, [elt])

    return tot_tuple


def make_tuple_v2(list_paths, size_tuple):
    """
    Return a list of tuples such that for each tuple, each element in `list_paths` has at least one element from the tuple.

    Args:
    - list_paths (List[List[Any]]): The list of paths connecting two color points.
    - size_tuple (int): The maximum size of the searched tuples.

    Goal: To determine the tuples representing mandatory passages in the list of paths connecting two color points.
    """
    if size_tuple == 0 or not list_paths:
        return []

    tot_tuple = []

    def recursive_tuple_v2(m, len_m, size_tuple, actual_tuple):
        nonlocal tot_tuple
        if size_tuple == 0:
            tot_tuple.append(actual_tuple)
            return

        for elt in m[0]:
            new_tuple = actual_tuple.union({elt})
            if len_m > 1:
                recursive_tuple_v2(m[1:], len_m - 1, size_tuple - 1, new_tuple)
            else:
                tot_tuple.append(new_tuple)
    len_m = len(list_paths)
    for elt in list_paths[0]:
        recursive_tuple_v2(list_paths[1:], len_m - 1, size_tuple - 1, {elt})

    return tot_tuple


def make_tuple_v3(list_paths: List[List[Any]], size_tuple: int) -> List[set]:
    """
    Return a list of sets such that for each set, each element in `list_paths` has at least one element from the set.

    Args:
    - list_paths (List[List[Any]]): The list of paths connecting two color points.
    - size_tuple (int): The maximum size of the searched sets.

    Goal: To determine the sets representing mandatory passages in the list of paths connecting two color points.
    """
    if size_tuple == 0 or list_paths == []:
        return []

    def recursive_tuple(m: List[List[Any]], len_m: int, size_tuple: int, actual_tuple: List[Any]) -> None:
        nonlocal tot_tuple
        
        if any(elt in m[0] for elt in actual_tuple):
            if len_m == 1:
                tot_tuple.append(set(actual_tuple))
            else:
                recursive_tuple(m[1:], len_m - 1, size_tuple, actual_tuple)
        elif size_tuple > 0:
            if len_m == 1:
                for elt in m[0]:
                    actual_tuple.append(elt)
                    tot_tuple.append(set(actual_tuple))
                    actual_tuple.pop()
            else:
                for elt in m[0]:
                    actual_tuple.append(elt)
                    recursive_tuple(m[1:], len_m - 1, size_tuple - 1, actual_tuple)
                    actual_tuple.pop()

    tot_tuple = []
    len_paths = len(list_paths)
    for elt in list_paths[0]:
        recursive_tuple(list_paths[1:], len_paths - 1, size_tuple - 1, [elt])

    return tot_tuple




def make_tuple_v4(list_paths: List[List[Any]], size_tuple: int) -> List[set]:
    """
    Return a list of sets such that for each set, each element in `list_paths` has at least one element from the set.

    Args:
    - list_paths (List[List[Any]]): The list of paths connecting two color points.
    - size_tuple (int): The maximum size of the searched sets.

    Goal: To determine the sets representing mandatory passages in the list of paths connecting two color points.
    """
    if size_tuple == 0 or list_paths == []:
        return []

    def recursive_tuple(m: List[List[Any]], len_m: int, size_tuple: int, actual_tuple: List[Any]) -> None:
        nonlocal tot_tuple
        
        if any(elt in m[0] for elt in actual_tuple):
            if len_m == 1:
                tot_tuple.append(set(actual_tuple))
            else:
                recursive_tuple(m[1:], len_m - 1, size_tuple, actual_tuple)
        elif size_tuple > 0:
            if len_m == 1:
                for elt in m[0]:
                    actual_tuple.append(elt)
                    tot_tuple.append(set(actual_tuple))
                    actual_tuple.pop()
            else:
                for elt in m[0]:
                    actual_tuple.append(elt)
                    recursive_tuple(m[1:], len_m - 1, size_tuple - 1, actual_tuple)
                    actual_tuple.pop()

    tot_tuple = []
    len_paths = len(list_paths)
    for elt in list_paths[0]:
        recursive_tuple(list_paths[1:], len_paths - 1, size_tuple - 1, [elt])

    return tot_tuple


# Exemple d'utilisation
paths = [[1, 2,8], [4,3,1,8], [4,5,6,8]]
# result = make_tuple(paths, 2)
result2 = make_tuple_v4(paths, 2)
# print(result)
print(result2)


# m = [[1,2,3],[2,3,4,5],[1,2,6,7,8]]
# paths = [[1, 2], [2, 3], [3, 4]]

# res = make_tuple_v2(paths, 2)
# print(m)
# print()
# print(res)
