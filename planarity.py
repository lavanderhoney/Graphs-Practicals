from graph_base import *

#adj_list will be a dict
def is_complete_graph(adj_matrix, n):
    """Check if a graph with n vertices is a complete graph (Kn)."""
    expected_edges = (n * (n - 1)) // 2  
    actual_edges = sum(sum(row) for row in adj_matrix) // 2  
    
    return actual_edges == expected_edges and all(sum(row) == (n - 1) for row in adj_matrix)

def is_bipartite_k33(adj_matrix):
    """Check if the graph is K3,3 (complete bipartite with two sets of 3 vertices)."""
    if len(adj_matrix) != 6:
        return False

    actual_edges = sum(sum(row) for row in adj_matrix) 
    if actual_edges != 9:  # K3,3 must have exactly 9 edges
        return False

    # Attempt to partition into two sets of size 3
    for subset in ([0, 1, 2], [3, 4, 5]):
        if all(adj_matrix[i][j] == 0 for i in subset for j in subset):
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

def homeomorphic_to_k5(adj_list):
    """Check if the graph is homeomorphic to K5"""
    
    

def edge_subdivision(adj_list, u, v):
    """Perform edge subdivision between the two given vertices u and v."""
    new_adj_list = adj_list.copy()
    new_node = max(adj_list) + 1
    new_adj_list[new_node] = [u, v]
    new_adj_list[u].remove(v)
    new_adj_list[v].remove(u)
    new_adj_list[u].append(new_node)
    new_adj_list[v].append(new_node)
    return new_adj_list

def edge_contract(adj_list, u):
    """Perform edge contraction on the given vertex u, which has exactly two neighbors."""
    new_adj_list = adj_list.copy()
    v, w = new_adj_list[u] #neighbors of u
    new_adj_list[v].remove(u)
    new_adj_list[w].remove(u)
    new_adj_list[v].add(w)
    new_adj_list[w].add(v)
    del new_adj_list[u]
    return new_adj_list
    
    
def check_self_loops(adj_list):
    """Check if the graph has self-loops."""
    return any(node in neighbors for node, neighbors in adj_list.items())

def check_parallel_edges(adj_list):
    """Check if the graph has parallel edges."""
    for node, neighbors in adj_list.items():
        temp_set = set()
        for neighbor in neighbors:
            if neighbor in temp_set:
                return True
            temp_set.add(neighbor)
    return False

def remove_degree_two_vertices(adj_list):
    """Removes degree 2 vertices by merging their neighbors."""
    to_remove = [node for node, neighbors in adj_list.items() if len(neighbors) == 2]
    for node in to_remove:
        u, v = list(adj_list[node])  # Two neighbors
        adj_list[u].remove(node)
        adj_list[v].remove(node)
        adj_list[u].add(v)
        adj_list[v].add(u)
        del adj_list[node]

k5_matrix = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

# K3,3 adjacency matrix (6x6)
k33_matrix = [
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0]
]

print(check_kurtowski_graph(k5_matrix))  
print(check_kurtowski_graph(k33_matrix))  


# g1 = Graph(4, 6, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2),
#                (1, 3)], is_undirected=True, is_weighted=False)
g1 = Graph(2,2, [(0,1), (1,0)], is_undirected=False, is_weighted=False)
g1.print_graph_nx()