def dls(graph, node, goal, depthlimit):
    print("Visiting:", node)
    
    
    if node == goal:
        return True
    
   
    if depthlimit <= 0:
        return False
    
    
    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depthlimit - 1):
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


start = 'A'
goal = 'E'
depthlimit = 2


found = dls(graph, start, goal, depthlimit)


if found:
    print("Goal Found")
else:
    print("Goal Not Found ") 