from collections import deque

# Goal state
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Possible moves (index shifts)
MOVES = {
    "UP": -3,
    "DOWN": 3,
    "LEFT": -1,
    "RIGHT": 1
}

def is_valid_move(index, move):
    row, col = divmod(index, 3)

    if move == "UP" and row == 0:
        return False
    if move == "DOWN" and row == 2:
        return False
    if move == "LEFT" and col == 0:
        return False
    if move == "RIGHT" and col == 2:
        return False

    return True


def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)

    for move, shift in MOVES.items():
        if is_valid_move(zero_index, move):
            new_index = zero_index + shift
            new_state = list(state)
            # Swap tiles
            new_state[zero_index], new_state[new_index] = (
                new_state[new_index],
                new_state[zero_index],
            )
            neighbors.append(tuple(new_state))

    return neighbors


def bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL_STATE:
            return path + [current_state]

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state]))

    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


if __name__ == "__main__":
    # Example starting state
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    solution = bfs(start)

    if solution:
        print(f"Solution found in {len(solution)-1} moves!\n")
        for step in solution:
            print_board(step)
    else:
        print("No solution found.")
