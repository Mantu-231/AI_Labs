import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor, path)
                )

    return float("inf"), []

# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
goal_node = 'D'

cost, path = uniform_cost_search(graph, start_node, goal_node)

print("Least cost:", cost)
print("Path:", " -> ".join(path))
