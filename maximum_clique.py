import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Function to check if a subset is a clique
def is_clique(graph, subset):
    """
    Check if the given subset of vertices forms a clique.
    Creates all possible pairs of vertices in the subset, and checks if each pair is connected.
    A clique is a subset of vertices such that every two distinct vertices are adjacent.
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
    Loops through all possible sizes of subsets of vertices, starting from largest(n) to smallest(1).
    For each size, it creates combinations of vertices of that size and checks if they form a clique. 
    The fisrst clique found is returned, and so it will be the largest one. 
    Args:
        graph (dict): Graph as an adjacency list.
    Returns:
        tuple: The largest clique found.
    """
    vertices = list(graph.keys())
    n = len(vertices)
    for k in range(n, 0, -1):
        for subset in itertools.combinations(vertices, k):
            if is_clique(graph, subset):
                return subset
    return None  # Return None if graph is empty


if __name__ == "__main__":
# Wheel graph W_5
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

    G = nx.from_dict_of_lists(graph)
    # Draw the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
    plt.title("Graph")
    plt.show()
    
    maximal_clique = find_maximal_clique(petersen_graph)
    print(f"Maximum clique: {maximal_clique}")