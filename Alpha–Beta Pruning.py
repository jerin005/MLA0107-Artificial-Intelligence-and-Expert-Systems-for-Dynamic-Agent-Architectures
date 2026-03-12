def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    # If leaf node reached
    if depth == 2:
        print("Leaf Node Value:", values[nodeIndex])
        return values[nodeIndex]

    if maximizingPlayer:
        best = -1000
        print("Maximizing Node at depth", depth)

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Pruning occurs at depth", depth)
                break

        return best

    else:
        best = 1000
        print("Minimizing Node at depth", depth)

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print("Pruning occurs at depth", depth)
                break

        return best


values = [3, 5, 6, 9]

result = alphabeta(0, 0, True, values, -1000, 1000)

print("Optimal Value:", result)
