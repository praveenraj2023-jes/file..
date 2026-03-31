from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node == target:
            return True
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                queue.append(neighbor)
    
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

target = 'E'

found = bfs(graph, 'A', target)

if found:
    print("Element Found using BFS")
else:
    print("Element Not Found using BFS")
