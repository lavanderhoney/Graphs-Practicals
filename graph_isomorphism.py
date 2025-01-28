from graph_base import *
import numpy as np

#------ Using permutaiton matrix to check isomorphism ------
np.random.seed(0)
# g1 = Graph(4,4 ,[(0, 1), (1, 2), (2, 3), (3, 0)], is_undirected=True, is_weighted=False)
# g2 = Graph(4,4, [(0, 2), (0, 3), (1, 2), (1, 3)], is_undirected=True, is_weighted=False)
g1 = Graph(6, 5, [(0,1), (1,2), (2,3), (3,4), (3,5)], is_undirected=True, is_weighted=False)
g2 = Graph(6, 5, [(0,1), (1,2), (2,3), (2,4), (2,5)], is_undirected=True, is_weighted=False)
g1.print_graph_nx()
g2.print_graph_nx()
# Create the permutation matrix
iter_ = 0
while iter_ < np.math.factorial(g1.V):
    P = [[0 for _ in range(g1.V)] for __ in range(g1.V)]
    select = np.random.permutation(g1.V)
    for i in range(g1.V):
        P[i][select[i]] = 1
    P = np.array(P)
    g1_permuted_adjmat = np.dot(np.dot(P, np.array(g1.adjacency_matrix)), P.T)
    if np.array_equal(g1_permuted_adjmat, np.array(g2.adjacency_matrix)):
        print("The graphs are isomorphic")
        print("The permutation matrix is: \n", P)
        print("The permuted adjacency matrix of g1 is: \n", g1_permuted_adjmat)
        print("The adjacency matrix of g2 is: \n", np.array(g2.adjacency_matrix))
        print("Permutation found after ", iter_, " iterations")
        break
    iter_ += 1

if iter_ == (np.math.factorial(g1.V)):
    print("The graphs are not isomorphic")
    print("Permutation not found after ", iter_, " iterations")