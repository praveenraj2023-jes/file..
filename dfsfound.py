def dfs(graph, node, target, visited):
    
    
    if node == target:
        return True
    
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    
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

found = dfs(graph, 'A', target, set())

if found:
    print("Element Found using DFS")
else:
    print("Element Not Found using DFS")