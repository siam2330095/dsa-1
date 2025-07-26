def has_cycle(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

# Example usage
n = 4
edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3)
]
print(has_cycle(n, edges))  # Output: True
