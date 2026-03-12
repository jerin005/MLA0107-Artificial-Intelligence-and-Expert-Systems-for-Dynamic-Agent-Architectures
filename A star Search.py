import heapq

graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',3), ('E',1)],
    'C': [('F',5)],
    'D': [],
    'E': [('F',2)],
    'F': []
}

heuristic = {
    'A':5, 'B':3, 'C':4,
    'D':2, 'E':1, 'F':0
}

def astar(start, goal):
    queue = [(0,start)]

    while queue:
        cost,node = heapq.heappop(queue)

        if node == goal:
            print("Reached Goal:",node)
            return

        for neighbor,weight in graph[node]:
            priority = weight + heuristic[neighbor]
            heapq.heappush(queue,(priority,neighbor))

astar('A','F')
