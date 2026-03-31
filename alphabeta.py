def alphabeta(depth, nodeIndex, isMax, values, alpha, beta):

    
    if depth == 3:
        return values[nodeIndex]

    
    if isMax:
        maxEval = -1000

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            False, values, alpha, beta)

            maxEval = max(maxEval, val)
            alpha = max(alpha, val)

            
            if beta <= alpha:
                break

        return maxEval

    
    else:
        minEval = 1000

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)

            minEval = min(minEval, val)
            beta = min(beta, val)

            # Pruning condition
            if beta <= alpha:
                break

        return minEval



values = [3, 5, 6, 9, 1, 2, 0, -1]


result = alphabeta(0, 0, True, values, -1000, 1000)

print("Optimal Value:", result)