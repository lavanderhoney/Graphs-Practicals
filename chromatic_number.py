from maximum_clique import find_maximal_clique
import networkx as nx
import matplotlib.pyplot as plt

# Function to check if it's safe to assign color c to vertex v
def is_safe(graph, color_assignment, v, c):
    """
    Check if assigning color c to vertex v conflicts with its neighbors.
    Args:
        graph (dict): Graph as an adjacency list.
        color_assignment (dict): Current color assignments.
        v: Vertex to color.
        c: Color to assign.
    Returns:
        bool: True if safe, False if there's a conflict.
    """
    for u in graph[v]:
        if color_assignment[u] is not None and color_assignment[u] == c:
            return False
    return True

# Backtracking function to attempt coloring with m colors
def backtrack(graph, color_assignment, v, m, n):
    """
    Recursively try to color the graph with m colors.
    Args:
        graph (dict): Graph as an adjacency list.
        color_assignment (dict): Current color assignments.
        v: Current vertex index (0 to n-1).
        m: Number of colors to use.
        n: Total number of vertices.
    Returns:
        bool: True if coloring succeeds, False otherwise.
    """
    if v == n:
        return True
    for c in range(m):
        if is_safe(graph, color_assignment, v, c):
            color_assignment[v] = c
            if backtrack(graph, color_assignment, v + 1, m, n):
                return True
            color_assignment[v] = None
    return False

def is_m_colorable(graph, m):
    """
    The main function to check if the graph can be colored with m colors.
    Args:
        graph (dict): Graph as an adjacency list.
        m: Number of colors.
    Returns:
        tuple: (bool, dict) - Whether m-colorable and the color assignment if so.
    """
    n = len(graph)
    color_assignment = {v: None for v in graph}
    if backtrack(graph, color_assignment, 0, m, n):
        return True, color_assignment
    return False, None

graph = {
        0: [1, 2, 3, 4],  # Central vertex
        1: [0, 2, 4],     # Cycle: 1-2-3-4-1
        2: [0, 1, 3],
        3: [0, 2, 4],
        4: [0, 1, 3]
    }
petersen_graph = {
        0: [1, 4, 5],
        1: [0, 2, 6],
        2: [1, 3, 7],
        3: [2, 4, 8],
        4: [0, 3, 9],
        5: [0, 7, 8],
        6: [1, 8, 9],
        7: [2, 5, 9],
        8: [3, 5, 6],
        9: [4, 6, 7]
}
maximal_clique = find_maximal_clique(petersen_graph)
k = len(maximal_clique)
m = k
while True:
    is_colorable, coloring = is_m_colorable(petersen_graph, m)
    if is_colorable:
        break
    m += 1
print(f"Chromatic number: {m}")

# Create a NetworkX graph from the dictionary
G = nx.from_dict_of_lists(petersen_graph)
some_color_list = ['red', 'blue', 'green', 'yellow', 'purple']
color_map = [some_color_list[coloring[node]] for node in G.nodes()]
pos = nx.shell_layout(G)
nx.draw(G, pos, node_color=color_map, with_labels=True)
plt.title("Wheel Graph W_5 with Optimal Coloring")
plt.show()