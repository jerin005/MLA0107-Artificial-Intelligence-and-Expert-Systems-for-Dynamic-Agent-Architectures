import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

def ucs(start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node == goal:
            print("Cost:", cost)
            return

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cost + weight, neighbor))

ucs('A', 'F')
