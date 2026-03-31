def dls(graph, node, goal, depth):
    
    if node == goal:
        return True
    
   
    if depth == 0:
        return False
    
    
    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depth - 1):
            return True
    
    return False


def idds(graph, start, goal, max_depth):
    
    for depth in range(max_depth + 1):
        print(f"\nSearching with depth limit = {depth}")
        
        if dls(graph, start, goal, depth):
            print(" Goal Found at depth", depth)
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
maxdepth = 3


result = idds(graph, start, goal, maxdepth)

if not result:
    print("Goal Not Found")