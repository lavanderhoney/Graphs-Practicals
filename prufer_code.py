from collections import defaultdict
from typing import Dict, Set, List
from graph_base import *
import heapq



def tree_to_pruffer(V: int, edges: Dict[int, Set]) -> List[int]:
    adj_list = dict()
    for i in range(1, V+1):
        adj_list[i] = set()
    
    for edge in edge_list:
        adj_list[edge[0]].add(edge[1])

    pruffer_code = []
    leafs = []
    killed = [False for _ in range(V)]
    for _ in range(1, V-1):
        for i in range(1, V+1):
            if len(adj_list[i])==0 and not killed[i-1]:
                heapq.heappush(leafs, i)
                killed[i-1] = True

        # print(leafs)
        leaf_node = heapq.heappop(leafs)
        for u, neighbours in adj_list.items():
            if leaf_node in neighbours:
                pruffer_code.append(u)
                adj_list[u].remove(leaf_node)

    # pruffer_code.sort()
    return pruffer_code

def prufer_to_tree(V:int, prufer_code: List[int])->List[List[int]]:
    """
    We use a property: each number in the Prüfer code represents a connection to a leaf node.
    1. Calculate the Degree of Each Vertex
        - The degree of a vertex is initially 1 plus the number of times it appears in the Prüfer sequence.
        - Any vertex not in the sequence has a degree of 1 (these are the leaves).
    2. Find the Smallest Leaf
        - A leaf is a vertex with a degree of 1.
        - The smallest leaf is the lowest-numbered vertex with degree 1.
        - So we store the leaf vertices in a min-heap (leafs).
    3. Build the Tree Iteratively
        For each number in the Prüfer code:
            - Connect the smallest leaf to the current Prüfer code number.
            - Decrease the degree of both vertices.
            - Find the next smallest leaf.
    4. Connect the Last Two Remaining Vertices
        After processing all Prüfer code numbers, exactly two vertices will remain with a degree of 1.
        Connect them to complete the tree.
    """

    edge_list = []
    leafs = []
    degree = [1 for _ in range(V)] #this degree is a count of how many edges that vertex must eventually have
    for node in prufer_code:
        degree[node-1] +=1
    
    for i in range(V):
        if degree[i]==1:
            heapq.heappush(leafs, i+1)
    
    for v in prufer_code:
        leaf_node = heapq.heappop(leafs)
        edge_list.append([v, leaf_node])
        degree[v-1] -=1
        if degree[v-1] ==1:
            heapq.heappush(leafs, v)

    edge_list.append([heapq.heappop(leafs),V])
    return edge_list

if __name__ == "__main__":
    edge_list = [[1,2],[1,4],[1,10],[4,3],[4,5],[5,6],[5,8],[8,7],[8,9]]

    print("Input number of vertices: ")
    V=int(input())
    
    E = len(edge_list)
    prufer_code = tree_to_pruffer(edge_list)
    tree_ = prufer_to_tree(prufer_code)
    print(tree_)
