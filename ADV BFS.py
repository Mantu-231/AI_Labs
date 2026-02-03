from collections import deque

# Graph representation using adjacency list
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

def bfs(start, goal):
    queue = deque([start])
    visited = []
    parent = {start: None}

    print("Source Node:", start)
    print("\nVertices:")
    for node in graph:
        print(node, end=" ")
    
    print("\n\nEdges:")
    for node in graph:
        for child in graph[node]:
            print(f"{node} -> {child}")

    while queue:
        current = queue.popleft()
        visited.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                parent[neighbor] = current
                queue.append(neighbor)

    # Path reconstruction
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    # Non-visited nodes
    non_visited = [node for node in graph if node not in visited]

    print("\nVisited Nodes:")
    print(visited)

    print("\nNon-Visited Nodes:")
    print(non_visited)

    print("\nPath from A to L:")
    print(" -> ".join(path))


# Driver code
start_state = 'A'
goal_state = 'L'
bfs(start_state, goal_state)
