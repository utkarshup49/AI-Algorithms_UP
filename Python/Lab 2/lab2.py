graph = {
    "Arad": [
        ("Zerind", 75),
        ("Sibiu", 140),
        ("Timisoara", 118)
    ],
    "Zerind": [
        ("Arad", 75),
        ("Oradea", 71)
    ],
    "Oradea": [
        ("Zerind", 71),
        ("Sibiu", 151)
    ],
    "Sibiu": [
        ("Arad", 140),
        ("Oradea", 151),
        ("Fagaras", 99),
        ("Rimnicu Vilcea", 80)
    ],
    "Timisoara": [
        ("Arad", 118),
        ("Lugoj", 111)
    ],
    "Lugoj": [
        ("Timisoara", 111),
        ("Mehadia", 70)
    ],
    "Mehadia": [
        ("Lugoj", 70),
        ("Dobreta", 75)
    ],
    "Dobreta": [
        ("Mehadia", 75),
        ("Craiova", 120)
    ],
    "Craiova": [
        ("Dobreta", 120),
        ("Rimnicu Vilcea", 146),
        ("Pitesti", 138)
    ],
    "Rimnicu Vilcea": [
        ("Sibiu", 80),
        ("Craiova", 146),
        ("Pitesti", 97)
    ],
    "Fagaras": [
        ("Sibiu", 99),
    ],
    "Pitesti": [
        ("Rimnicu Vilcea", 97),
        ("Craiova", 138),
        ("Bucharest", 101)
    ],
    "Bucharest": [
        ("Fagaras", 211),
        ("Pitesti", 101),
        ("Giurgiu", 90),
        ("Urziceni", 85)
    ],
    "Giurgiu": [
        ("Bucharest", 90)
    ],
    "Urziceni": [
        ("Bucharest", 85),
        ("Hirsova", 98),
        ("Vaslui", 142)
    ],
    "Hirsova": [
        ("Urziceni", 98),
        ("Eforie", 86)
    ],
    "Eforie": [
        ("Hirsova", 86)
    ],
    "Vaslui": [
        ("Urziceni", 142),
        ("Iasi", 92)
    ],
    "Iasi": [
        ("Vaslui", 92),
        ("Neamt", 87)
    ],
    "Neamt": [
        ("Iasi", 87)
    ]
}

heuristic = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

def best_first(graph, heuristic, start, goal):
    open_list = [(start, [start])]
    closed = []

    while open_list:
        open_list.sort(key=lambda x: heuristic[x[0]])
        current, path = open_list.pop(0)

        if current == goal:
            return path

        closed.append(current)

        for neighbor, _ in graph[current]:
            if neighbor not in closed:
                open_list.append((neighbor, path + [neighbor]))

    return None

def a_star(graph, heuristic, start, goal):
    open_list = [(start, 0, [start])]
    closed = []

    while open_list:
        open_list.sort(key=lambda x: x[1] + heuristic[x[0]])
        current, g_cost, path = open_list.pop(0)

        if current == goal:
            return path, g_cost

        if current in closed:
            continue

        closed.append(current)

        for neighbor, cost in graph[current]:
            if neighbor not in closed:
                open_list.append(
                    (neighbor, g_cost + cost, path + [neighbor])
                )

    return None, None


import random
import math

def simulated_annealing(graph, heuristic, start, goal,
                        T=1000.0, cooling=0.995, Tmin=1e-3):

    def path_cost(path):
        c = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for n, w in graph[u]:
                if n == v:
                    c += w
                    break
        return c

    current = [start]
    current_cost = heuristic[start]
    best = current
    best_cost = float("inf")

    while T > Tmin:
        if current[-1] == goal:
            g = path_cost(current)
            if g < best_cost:
                best, best_cost = current, g
            break

        next_nodes = [
            current + [n]
            for n, _ in graph[current[-1]]
            if n not in current
        ]
        if not next_nodes:
            break

        candidate = random.choice(next_nodes)
        g = path_cost(candidate)
        f = g + heuristic[candidate[-1]]

        delta = f - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = candidate
            current_cost = f

        T *= cooling

    return best, best_cost


if __name__ == '__main__':
    path = best_first(graph, heuristic, "Arad", "Bucharest")
    print(path)

    path, total_cost = a_star(graph, heuristic, "Arad", "Bucharest")
    print(path)
    print(total_cost)

    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": []
    }

    heuristic = {
        "A": 4,
        "B": 3,
        "C": 1,
        "D": 0
    }

    start = "A"
    goal = "D"

    best_path, best_cost = simulated_annealing(
        graph,
        heuristic,
        start,
        goal,
        T=100,
        cooling=0.9,
        Tmin=0.01
    )

    print(best_path)
    print(best_cost)

    # path, cost = simulated_annealing(graph, heuristic, "Arad", "Bucharest")
    # print(path)
    # print(cost)
