from collections import defaultdict
from graph_base import *

class GraphOps():
    #assume the vertices of G1 and G2 will have same labelling or numbering, like 0,1,2 etc...
    def __init__(self):
        pass

    def union(g1, g2):
        """Computes the union of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the union of g1 and g2
        """
        R_adjlist = defaultdict(set)
        R_vertices = set()
        g1_adjlist = g1.adjacency_list
        g2_adjlist = g2.adjacency_list

        for node in g1_adjlist:
            R_adjlist[node].update(g1_adjlist[node])
            R_vertices.add(node)
        for node in g2_adjlist:
            R_adjlist[node].update(g2_adjlist[node])
            R_vertices.add(node)


        R_adjlist = dict(R_adjlist)
        R_edges = get_edges_list(R_adjlist)
        R = Graph(
            V = len(R_vertices),
            is_weighted = g1.is_weighted,
            is_undirected = g1.is_undirected,
            edges_list = R_edges
        )

        return R
    
    def intersection(g1, g2):
        """Computes the R of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the intersection of g1 and g2
        """
        R_graph_adjlist = defaultdict(set)
        R_graph_vertices = set()
        g1_adjlist = g1.adjacency_list
        g2_adjlist = g2.adjacency_list

        for node in g1_adjlist:
            if node in g2_adjlist:
                R_graph_adjlist[node].update(g1_adjlist[node] & g2_adjlist[node])
                R_graph_vertices.add(node)

        R_graph_adjlist = dict(R_graph_adjlist)
        R_graph_edges = get_edges_list(R_graph_adjlist)
        R = Graph(
            V = len(R_graph_vertices),
            is_weighted = g1.is_weighted,
            is_undirected = g1.is_undirected,
            edges_list = R_graph_edges
        )

        return R
    
    def difference(g1, g2):
        """Computes the difference of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the difference of g1 and g2
        """
        R_graph_adjlist = defaultdict(set)
        R_graph_vertices = set()
        g1_adjlist = g1.adjacency_list
        g2_adjlist = g2.adjacency_list

        for node in g1_adjlist:
            if node not in g2_adjlist:
                R_graph_adjlist[node].update(g1_adjlist[node])
                R_graph_vertices.add(node)

        R_graph_adjlist = dict(R_graph_adjlist)
        R_graph_edges = get_edges_list(R_graph_adjlist)
        R = Graph(
            V = len(R_graph_vertices),
            is_weighted = g1.is_weighted,
            is_undirected = g1.is_undirected,
            edges_list = R_graph_edges
        )

        return R
    
    def ringsum(self,g1, g2):
        """Computes the ringsum of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the ringsum of g1 and g2
        """
        # R_graph_adjlist = defaultdict(set)
        # R_graph_vertices = set()
        R_union = self.union(g1, g2)
        R_intersection = self.intersection(g1, g2)
        R = self.difference(R_union, R_intersection)
        return R


def get_adjacency_list(edges_list):
    adj_list = defaultdict(set)
    for edge in edges_list:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])
    return dict(adj_list)

def get_edges_list(adj_list):
    edges_list = []
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            edges_list.append((node, neighbor))
    return edges_list
# Example usage
# graph1 = [(0, 1), (0, 2), (1, 3)]
# graph1_adj_list = get_adjacency_list(graph1)
# g1 = nx.from_edgelist(graph1)
# nx.draw(g1, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15, font_color='black')
# plt.title("Graph 1")
# plt.show()

# graph2 = [(0, 1), (0, 3), (2, 3)]
# graph2_adj_list = get_adjacency_list(graph2)
# g2 = nx.from_edgelist(graph2)
# nx.draw(g2, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15, font_color='black')
# plt.title("Graph 2")
# plt.show()


