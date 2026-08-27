def dfs(graph , start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in  graph[start]:
        if neighbor not in visited:
                dfs(graph,neighbor,visited)

        
graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []

}
visited = set()
dfs(graph, 'A', visited)

# # time complexity is  O(V+E) where V is the number of vertices and E is the number of edges in the graph.

