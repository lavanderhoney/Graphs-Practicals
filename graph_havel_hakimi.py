from graph_base import *
import numpy as np

def check_graphical(degree_seq):
    """
    Havel-Hakimi theorem: A sequence is graphic if and only if the sequence obtained by deleting the largest degree k 
    and subtracting one to the k largest degrees remaining is graphic.
    A degree sequence is graphic is there exists a simple graph with that degree sequence.
    """
    degree_seq = degree_seq.copy()
    
    #theorem: sum of degree sequence must be even
    if sum(degree_seq) % 2 != 0:
        return False
    
    for i in range(len(degree_seq)):
        for j in range(i, len(degree_seq)):
            if degree_seq[j] <0:
                return False #degree sequence must be non-negative
        
        #check if all elements are zero. If all elements are zero, then the degree sequence is graphic
        check_zero=True
        for j in range(i, len(degree_seq)):
            if degree_seq[j] != 0:
                check_zero = False
        if check_zero:
            return True
        
        #every time we remove a vertex, we need to decrement the degree of the next k vertices. The next vertex is implemented wtih j=i+1
        #where k is the degree of the vertex we removed
        for j in range(i+1, len(degree_seq)):
            degree_seq[j] -= 1

        
    print(degree_seq)

def degree_seq_to_graph(degree_seq):
    #assume degree_seq is sorted in descending order

    vertices = len(degree_seq)
    edge_list = []
    for i in range(vertices):
        for j in range(i+1, vertices):
            if degree_seq[i] > 0 and degree_seq[j] > 0:
                edge_list.append((i, j))
                degree_seq[i] -= 1
                degree_seq[j] -= 1
        degree_seq.sort(reverse=True)
    print(edge_list)
    return Graph(V=vertices, E=len(edge_list), edges=edge_list, is_undirected=False, is_labelled=False)
    
g1 = Graph(V=5,
           E=6,
           edges=[(0, 1), (0, 2), (1, 2),
                  (1, 3), (2, 4), (3, 4)],
           is_labelled=False)

g1.print_graph_nx()

degree_seq = sorted([sum(x) for x in g1.adjacency_matrix], reverse=True)
print(degree_seq)

if check_graphical(degree_seq):
    g2 = degree_seq_to_graph(degree_seq)
    g2.print_graph_nx()
else:
    print("Graphical sequence does not exist")

