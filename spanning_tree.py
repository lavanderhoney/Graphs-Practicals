from prufer_code import *
from typing import Tuple
import copy
import networkx as nx

def generate_pruffer_sequence(n, prufer_sequences, sequence, seq_len):
    if seq_len == n-2:
        sequence_ = list(sequence)
        prufer_sequences.append(sequence_)
        return prufer_sequences
    for num in range(1, n+1):
        #back tracking
        sequence.append(num)
        seq_len+=1
        prufer_sequences = generate_pruffer_sequence(n, prufer_sequences, sequence, seq_len)
        sequence.remove(num)
        seq_len-=1
    return prufer_sequences

def check_valid_tree(V: int, edges: List[Tuple[int]]) -> bool:
    if len(edges) != V-1:
        return False
    
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    if len(vertices) != V:
        return False
    temp_graph = nx.Graph()
    temp_graph.add_edges_from(edges)
    return nx.is_connected(temp_graph)

def spanning_tree_edges(V: int, 
                        idx: int,
                        edges_list: List[Tuple[int]], 
                        all_trees : List[List[Tuple[int]]], 
                        tree: List[Tuple[int]]) -> List[List[Tuple[int]]]:
    
    if len(tree) == V-1 or idx>=len(edges_list):
        if check_valid_tree(V, tree):
            all_trees.append(copy.copy(tree))
            # print(all_trees)
        return all_trees
    
    edge = edges_list[idx]

    #include
    tree.append(edge)
    idx+=1
    all_trees = spanning_tree_edges(V,idx, edge_list, all_trees, tree)

    #exclude
    tree.remove(edge)
    all_trees = spanning_tree_edges(V,idx, edge_list, all_trees, tree)

    return all_trees

if __name__ == "__main__":
    n=5
    prufer_sequences = generate_pruffer_sequence(n, prufer_sequences=[], sequence=[], seq_len=0)

    all_spanning_trees = []
    for prufer_code in prufer_sequences:
        all_spanning_trees.append(prufer_to_tree(n, prufer_code))

    print("\nAll possible spaning trees (connected graph):")
    for tree in all_spanning_trees:
        print(tree)

    edge_list = [(0,1),(1,2),(2,3),(3,0),(3,4),(3,5),(2,5)]
    V = 6
    edge_list.sort()
    all_possible_trees = spanning_tree_edges(V, 0, edge_list, [], [])
    print("\nAll possible spanning trees, given a graph: ")
    for tree in all_possible_trees:
        print(tree)