from dijkstra import dijkstra

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start = 'C'
distances = dijkstra(graph, start)
print(f"\nВідстань між вершинами в точки {start}:\n{distances}")
