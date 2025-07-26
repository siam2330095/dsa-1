from collections import deque

def has_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 0 or grid[rows - 1][cols - 1] == 0:
        return False  # No path if start or end is a wall
    queue = deque()
    queue.append((0, 0))
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True

    # directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        # Reached the goal
        if x == rows - 1 and y == cols - 1:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check bounds and if it's a path and not visited
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return False
