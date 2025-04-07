import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Function to check if a subset is a clique
def is_clique(graph, subset):
    """
    Check if the given subset of vertices forms a clique.
    Args:
        graph (dict): Graph as an adjacency list.
        subset (tuple): Subset of vertices to check.
    Returns:
        bool: True if the subset is a clique, False otherwise.
    """
    for u, v in itertools.combinations(subset, 2):
        if v not in graph[u]:
            return False
    return True

# Function to find the maximum clique
def find_maximal_clique(graph):
    """
    Find the largest clique using a brute-force approach.
    Args:
        graph (dict): Graph as an adjacency list.
    Returns:
        tuple: The largest clique found.
    """
    vertices = list(graph.keys())
    n = len(vertices)
    # Check subsets from largest to smallest
    for k in range(n, 0, -1):
        for subset in itertools.combinations(vertices, k):
            if is_clique(graph, subset):
                return subset
    return None  # Return None if graph is empty

#wheel graph W_5
graph = {
    0: [1, 2, 3, 4],  # Central vertex
    1: [0, 2, 4],     # Cycle: 1-2-3-4-1
    2: [0, 1, 3],
    3: [0, 2, 4],
    4: [0, 1, 3]
}

# Find and print the maximum clique
maximal_clique = find_maximal_clique(graph)
print(f"Maximum clique: {maximal_clique}")

# Create a NetworkX graph from the dictionary
G = nx.from_dict_of_lists(graph)

# Define node colors: red for clique vertices, blue for others
color_map = ['red' if node in maximal_clique else 'blue' for node in G.nodes()]
pos = nx.shell_layout(G, nlist=[[0], [1, 2, 3, 4]])

# Draw the graph with labels
nx.draw(G, pos, node_color=color_map, with_labels=True)
plt.title("Wheel Graph W_5 with Maximum Clique Highlighted")
plt.show()