import heapq

# Step 1: Define graph with costs
graph = {
    'A': [('B',1), ('C',4)],
    'B': [('D',2), ('E',5)],
    'C': [('F',3)],
    'D': [],
    'E': [('F',1)],
    'F': []
}

# Step 2: UCS function
def ucs(start, goal):

    queue = [(0, start)]   # priority queue
    visited = set()

    while queue:

        cost, node = heapq.heappop(queue)  # lowest cost node

        print("Visiting Node:", node, "with Cost:", cost)

        if node == goal:
            print("Goal Reached:", node)
            print("Total Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                heapq.heappush(queue,(cost + weight, neighbor))

# Step 3: Call UCS
ucs('A','F')
