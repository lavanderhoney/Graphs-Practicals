from collections import defaultdict
from graph_base import *

class GraphOps():

    #assume the vertices of G1 and G2 will have same labelling or numbering, like 0,1,2 etc...

    def __init__(self):
        pass
    
    def get_adjacency_list(self,edges_list):
        adj_list = defaultdict(set)
        for edge in edges_list:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        return dict(adj_list)

    def get_edges_list(self,adj_list):
        edges_list = []
        for node, neighbors in adj_list.items():
            for neighbor in neighbors:
                edges_list.append((node,neighbor[0]))
        return edges_list
    
    def union(self,g1, g2):
        """Computes the union of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the union of g1 and g2
        """
        g1_adjlist = g1.adjacency_list 
        g2_adjlist = g2.adjacency_list

        #Find the number of vertices in the union graph
        R_vertices = set()  
        for node, edges in enumerate(g1_adjlist):
            R_vertices.add(node)
        for node, edges in enumerate(g2_adjlist):
            R_vertices.add(node)

        R_adjlist = [set() for _ in range(len(R_vertices))] #list of sets
        for node, edges in enumerate(g1_adjlist):
            for edge in edges:
                R_adjlist[node].add(edge)
        for node, edges in enumerate(g2_adjlist):
            for edge in edges:
                R_adjlist[node].add(edge)

        R_adjlist = dict(enumerate(R_adjlist))
        R_edges = self.get_edges_list(R_adjlist)
        R = Graph(
            V = len(R_vertices),
            E = len(R_edges),
            is_weighted = g1.is_weighted,
            is_undirected = g1.is_undirected,
            edges= R_edges
        )

        return R
    
    def intersection(self, g1, g2):
        """Computes the R of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the intersection of g1 and g2
        """
        g1_adjlist = g1.adjacency_list 
        g2_adjlist = g2.adjacency_list

        #Find the common vertices
        R_vertices = set()  
        for node, edges in enumerate(g1_adjlist):
            R_vertices.add(node)
        for node, edges in enumerate(g2_adjlist):
            R_vertices.add(node)
        
        R_adjlist = [set() for _ in range(len(R_vertices))] #list of sets
        for node, edges in enumerate(g1_adjlist):
            for edge in edges:
                if edge in g2_adjlist[node]:
                    R_adjlist[node].add(edge)

        R_adjlist = dict(enumerate(R_adjlist))
        R_edges = self.get_edges_list(R_adjlist)
        R = Graph(
            V = len(R_vertices),
            E = len(R_edges),
            is_weighted = g1.is_weighted,
            is_undirected = g1.is_undirected,
            edges= R_edges
        )

        return R
    
    def difference(self, g1, g2):
        """Computes the difference of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the difference of g1 and g2
        """
        g1_adjlist = g1.adjacency_list 
        g2_adjlist = g2.adjacency_list

        #Find the number of vertices in the difference graph
        R_vertices = set()  
        for node, edges in enumerate(g1_adjlist):
            R_vertices.add(node)
        for node, edges in enumerate(g2_adjlist):
            R_vertices.add(node)
        
        R_adjlist = [set() for _ in range(len(R_vertices))] #list of sets
        for node, edges in enumerate(g1_adjlist):
            for edge in edges:
                if edge not in g2_adjlist[node]:
                    R_adjlist[node].add(edge)

        R_adjlist = dict(enumerate(R_adjlist))
        R_edges = self.get_edges_list(R_adjlist)
        R = Graph(
            V = len(R_vertices),
            E = len(R_edges),
            is_weighted = g1.is_weighted,
            is_undirected = g1.is_undirected,
            edges = R_edges
        )
        return R
    
    def ringsum(self,g1, g2):
        """Computes the ringsum of two graphs represented as adjacency lists.
        g1: Graph object (from graph_base.py) of graph 1
        g2: Graph object (from graph_base.py) of graph 2

        returns: R, a Graph object of the ringsum of g1 and g2
        """
        # R_adjlist = defaultdict(set)
        # R_graph_vertices = set()
        R_union = self.union(g1, g2)
        R_intersection = self.intersection(g1, g2)
        R = self.difference(R_union, R_intersection)
        return R

gops = GraphOps()

# add labels to the edges after testing
g1 = Graph(V=5,
           E=6, 
           edges=[(0, 1),(0,2),(1,2),(1,3),(2,4),(3,4)])

g2 = Graph(V=6, 
           E=6,
           edges=[(0,1),(0,2),(1,2),(1,5),(2,5),(5,4)])

g1.print_graph_nx()
g2.print_graph_nx()

R_union = gops.union(g1, g2)
R_union.print_graph_nx()

R_intersection = gops.intersection(g1, g2)
R_intersection.print_graph_nx()

R_difference = gops.difference(g1, g2)
R_difference.print_graph_nx()

R_ringsum = gops.ringsum(g1, g2)
R_ringsum.print_graph_nx()
# plt.show()


