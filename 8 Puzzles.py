from collections import deque

# Goal State
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Function to find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to generate new states
def generate_states(state):
    x, y = find_blank(state)
    moves = [(0,1), (0,-1), (1,0), (-1,0)]
    children = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            children.append(new_state)

    return children

# BFS Algorithm
def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current, path = queue.popleft()

        if current == goal_state:
            return path + [current]

        visited.add(str(current))

        for child in generate_states(current):
            if str(child) not in visited:
                queue.append((child, path + [current]))

    return None

# Initial State
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

# Solve the puzzle
solution = bfs(initial_state)

# Print Solution
if solution:
    print("Solution Path:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
