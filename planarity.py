from graph_base import *
import networkx as nx
import matplotlib.pyplot as plt

def display_graph(adj_list, title="Graph"):
    G = nx.Graph()
    for node, neighbors in adj_list.items():
        G.add_node(node)
        for neigh in neighbors:
            if not G.has_edge(node, neigh):
                G.add_edge(node, neigh)
    plt.figure(figsize=(4, 4))
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500)
    plt.title(title)
    plt.show()

def is_complete_graph(adj_matrix, n):
    """Check if a graph with n vertices is a complete graph (Kn)."""
    expected_edges = (n * (n - 1)) // 2  
    actual_edges = sum(sum(row) for row in adj_matrix) // 2  
    return actual_edges == expected_edges and all(sum(row) == (n - 1) for row in adj_matrix)

def is_bipartite_k33(adj_matrix):
    """Check if the graph is K3,3 (complete bipartite with two sets of 3 vertices)."""
    if len(adj_matrix) != 6:
        return False
    actual_edges = sum(sum(row) for row in adj_matrix)  # Should be 18 (9 edges, undirected graph counts both directions)
    if actual_edges != 18:  # K3,3 has 9 edges, so 18 in symmetric matrix
        return False
    # Attempt to partition into two sets of size 3 (simplified check)
    for subset in ([0, 1, 2], [3, 4, 5]):
        if all(adj_matrix[i][j] == 0 for i in subset for j in subset):  # No edges within subset
            return True
    return False

def check_kurtowski_graph(adj_matrix):
    """Determine if a given adjacency matrix represents K5 or K3,3."""
    n = len(adj_matrix)
    if n == 5 and is_complete_graph(adj_matrix, 5):
        return "The graph is K5"
    if n == 6 and is_bipartite_k33(adj_matrix):
        return "The graph is K3,3"
    return "The graph is neither K5 nor K3,3"

def check_self_loops(adj_list):
    """Check if the graph has self-loops."""
    return any(node in neighbors for node, neighbors in adj_list.items())

def remove_self_loops(adj_list):
    """Removes self-loops from the graph."""
    return {node: {neighbor for neighbor in neighbors if neighbor != node} for node, neighbors in adj_list.items()}

# Corrected elementary_reduction function with planarity check
def elementary_reduction(adj_list):
    """
    Applies reduction steps:
      - Remove self-loops.
      - Remove parallel edges (handled by set representation).
      - Remove degree-two vertices by merging their neighbors.
    After each iteration, displays the graph.
    Finally, checks if the reduced graph is K5 or K3,3 to determine planarity.
    Returns the reduced graph.
    """
    # Convert adjacency list to use sets for neighbors
    current_graph = {node: set(neighbors) for node, neighbors in adj_list.items()}
    iteration = 0
    is_changed = True
    
    while is_changed:
        iteration += 1
        print(f"Iteration {iteration}:")
        print(current_graph)
        
        is_changed = False
        
        # Step 1: Remove self-loops
        if check_self_loops(current_graph):
            current_graph = remove_self_loops(current_graph)
            is_changed = True
        
        # Step 2: Remove parallel edges
        # Already handled by using set representation
        
        # Step 3: Eliminate degree-two vertices
        to_remove = [node for node, neighbors in current_graph.items() if len(neighbors) == 2]
        for node in to_remove:
            if node in current_graph:  # Check if node still exists
                u, v = list(current_graph[node])  # Two neighbors
                current_graph[u].remove(node)
                current_graph[v].remove(node)
                current_graph[u].add(v)
                current_graph[v].add(u)
                del current_graph[node]
                is_changed = True
        
        display_graph(current_graph, title=f"After reduction iteration {iteration}")
    
    # After reduction, convert to adjacency matrix for planarity check
    vertices = sorted(current_graph.keys())
    m = len(vertices)
    if m == 0:  # Empty graph is planar
        print("The original graph is planar")
    else:
        # Create adjacency matrix
        index_map = {old_label: new_index for new_index, old_label in enumerate(vertices)}
        adj_matrix = [[0] * m for _ in range(m)]
        for old_u in current_graph:
            new_u = index_map[old_u]
            for old_v in current_graph[old_u]:
                new_v = index_map[old_v]
                adj_matrix[new_u][new_v] = 1
                adj_matrix[new_v][new_u] = 1  # Ensure symmetry for undirected graph
        
        # Check if reduced graph is K5 or K3,3
        result = check_kurtowski_graph(adj_matrix)
        if result == "The graph is K5" or result == "The graph is K3,3":
            print("The original graph is non-planar")
        else:
            print("The original graph is planar")
    
    return current_graph

if __name__ == "__main__":
    k5 = {
        0: {1, 2, 3, 4},
        1: {0, 2, 3, 4},
        2: {0, 1, 3, 4},
        3: {0, 1, 2, 4},
        4: {0, 1, 2, 3}
    }
    print("Testing K5:")
    reduced = elementary_reduction(k5)
    
    g2 = {
        0: {1, 2, 3, 4},
        1: {0, 2, 3, 4},
        2: {0, 1, 3, 4},
        3: {0, 1, 2, 4},
        4: {0, 1, 2, 3, 5},
        5: {4} 
    }
    print("\nTesting G2:")
    reduced = elementary_reduction(g2)
    # Example: Triangle (K3, planar)
    # triangle = {
    #     0: {1, 2},
    #     1: {0, 2},
    #     2: {0, 1}
    # }
    # print("\nTesting Triangle (K3):")
    # reduced = elementary_reduction(triangle)