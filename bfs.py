from collections import deque

def bfs(graph, start):
    visited = set()       
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node,end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}   

bfs(graph, 'A')



def level(root):
    if not root:
        return []
    result =[]
    queue = deque([root])
    while len(queue) >0:
        level=[]
        for i in range(len(queue)):
            node =queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result   

 