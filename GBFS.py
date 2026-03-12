import heapq

# Step 1: Define graph
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Step 2: Define heuristic values
heuristic = {
    'A':5,
    'B':3,
    'C':4,
    'D':2,
    'E':1,
    'F':0
}

# Step 3: GBFS function
def gbfs(start, goal):

    queue = [(heuristic[start], start)]
    visited = set()

    while queue:

        h, node = heapq.heappop(queue)

        print("Visiting Node:", node, "Heuristic:", h)

        if node == goal:
            print("Goal Reached:", node)
            return

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                heapq.heappush(queue,(heuristic[neighbor],neighbor))

# Step 4: Call function
gbfs('A','F')
