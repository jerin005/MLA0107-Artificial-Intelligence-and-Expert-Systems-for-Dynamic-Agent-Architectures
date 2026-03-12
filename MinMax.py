from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == 2 or y == 2:
            print("Goal Reached")
            return

        # Possible states
        queue.append((4, y))  # Fill 4L jug
        queue.append((x, 3))  # Fill 3L jug
        queue.append((0, y))  # Empty 4L jug
        queue.append((x, 0))  # Empty 3L jug

        # Pour 4L → 3L
        pour = min(x, 3 - y)
        queue.append((x - pour, y + pour))

        # Pour 3L → 4L
        pour = min(y, 4 - x)
        queue.append((x + pour, y - pour))

water_jug()
