import heapq  

def ucs(graph, start, goal):
    
    queue = [(0, start)]
    
    
    visited = {}
    
    while queue:
        
        cost, node = heapq.heappop(queue)
        
        
        if node in visited and visited[node] <= cost:
            continue
        
        
        visited[node] = cost
        
        print(f"Visiting: {node} with cost: {cost}")
        
        
        if node == goal:
            print("Goal Reached!")
            return cost
        
        
        for neighbor, weight in graph[node]:
            heapq.heappush(queue, (cost + weight, neighbor))
    
    return float("inf")



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': []
}


start = 'A'
goal = 'E'


mincost = ucs(graph, start, goal)


print("Minimum Cost to reach goal:", mincost)
