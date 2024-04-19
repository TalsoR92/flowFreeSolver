
def dots_path(board, positions):
        start_pos = positions[0]
        visited = set()
        paths = []

        def dfs(current_pos, color, path):
            visited.add(current_pos)
            path.append(current_pos)

            if current_pos == end_pos:
                paths.append(path[:])
            else:
                valid, neighbors = board.available_cases_for_dfs(current_pos, color, visited)
                if valid:
                    for neighbor in neighbors:
                        dfs(neighbor, color, path)

            path.pop()
            visited.remove(current_pos)

        color = board.board[start_pos.y][start_pos.x].color
        dfs(start_pos, color, [])

        return paths


def all_dots_path(board):
    list_all_path = []

    for color in board.pos_points:
        list_all_path.append(dots_path(board, board.pos_points[color]))
        break
    return list_all_path

