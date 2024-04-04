import time


def make_tuple(paths, len_tuple):
    if len_tuple == 0 or paths == []:
        return []
    tot_tuple = []
    len_paths = len(paths)
    for elt in paths[0]:
        list_tuple = []
        recursive_tuple(paths[1:], len_paths - 1, len_tuple - 1, list_tuple, [elt])
        if list_tuple != []:
            tot_tuple += list_tuple

    return tot_tuple

def recursive_tuple(m, len_m, size_tuple, list_tuple, actual_tuple):
    if any(elt in m[0] for elt in actual_tuple):
        if len_m == 1:
            list_tuple.append(actual_tuple.copy())
        else:
            recursive_tuple(m[1:], len_m - 1, size_tuple, list_tuple, actual_tuple)
    elif size_tuple > 0:
        if len_m == 1:
            for elt in m[0]:
                actual_tuple.append(elt)
                list_tuple.append(actual_tuple.copy())
                actual_tuple.pop()
        else:
            for elt in m[0]:
                actual_tuple.append(elt)
                recursive_tuple(m[1:], len_m - 1, size_tuple - 1, list_tuple, actual_tuple)
                actual_tuple.pop()



m = [[1,2,3],[2,3,4,5],[1,2,6,7,8]]

res = make_tuple(m, 2)
print(m)
print()
print(res)

