from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['I', 'J'],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['K', 'L'],
    'J': [],
    'K': [],
    'L': []
}

def bfs(start):
    visited = []
    queue = deque([start])

    print("Source Node:", start)
    print("\nBFS Traversal Order:")

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            print(current, end=" ")
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Driver code
start_state = 'A'
bfs(start_state)
