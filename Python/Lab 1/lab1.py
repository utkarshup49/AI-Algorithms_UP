def dfs(graph, start, target):
    stack, visited = [start], set()
    while stack:
        node = stack.pop()
        if node == target:
            print("DFS:", node)
            return
        visited.add(node)
        stack.extend(n for n in graph[node] if n not in visited and n not in stack)
    print("DFS: Not Found")


def bfs(graph, start, target):
    queue, visited = [start], set()
    while queue:
        node = queue.pop(0)
        if node == target:
            print("BFS:", node)
            return
        visited.add(node)
        queue.extend(n for n in graph[node] if n not in visited and n not in queue)
    print("BFS: Not Found")


def steepest_hill_climbing(graph, h, start, goal):
    current, visited = start, set()
    while True:
        print("HC:", current)
        if current == goal:
            print("HC: Found Goal")
            return
        visited.add(current)
        candidates = [n for n in graph[current] if n not in visited]
        if not candidates:
            print("HC: local minimum")
            return
        best = min(candidates, key=lambda n: h[n])
        if h[best] >= h[current]:
            print("HC: local minimum")
            return
        current = best


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['E', 'F'],
    'D': ['A'],
    'E': ['C', 'G'],
    'F': ['C', 'G'],
    'G': []
}

heuristic = {
    'A': 15,
    'B': 13,
    'C': 9,
    'D': 12,
    'E': 7,
    'F': 8,
    'G': 0
}

dfs(graph, 'A', 'G')
bfs(graph, 'A', 'G')
steepest_hill_climbing(graph, heuristic, 'A', 'G')
