def isValid(state):
    missionariesLeft, cannibalsLeft, boatSide = state
    
    missionariesRight = 3 - missionariesLeft
    cannibalsRight = 3 - cannibalsLeft

    
    if missionariesLeft < 0 or cannibalsLeft < 0 or missionariesLeft > 3 or cannibalsLeft > 3:
        return False

    
    if missionariesLeft > 0 and missionariesLeft < cannibalsLeft:
        return False

   
    if missionariesRight > 0 and missionariesRight < cannibalsRight:
        return False

    return True


def dfs(state, goal, visited, path):
    path.append(state)
    visited.add(state)

    
    if state == goal:
        return True

    missionariesLeft, cannibalsLeft, boatSide = state

    
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for m, c in moves:
        if boatSide == 1:  
            newState = (missionariesLeft - m, cannibalsLeft - c, 0)
        else:              
            newState = (missionariesLeft + m, cannibalsLeft + c, 1)

        if isValid(newState) and newState not in visited:
            if dfs(newState, goal, visited, path):
                return True

    
    path.pop()
    return False


start = (3, 3, 1)
goal = (0, 0, 0)

visited = set()
path = []


if dfs(start, goal, visited, path):
    print("Solution Path:")
    for step in path:
        print(step)
else:
    print("No solution found")
