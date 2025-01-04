import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

class GraphView():
    def __init__(self, V, E, edges):
        self.V = V # number of vertices
        self.E = E # number of edges
        self.edges_list = edges # list of edges
        self.adjacency_list = [[] for _ in range(self.V)]
        self.adjacency_matrix = [[0 for _ in range(self.V)] for __ in range(self.V)]
        self.incidence_matrix = [[0 for _ in range(self.E)] for __ in range(self.V)]
        self.update_all_views(1)

    #provide lists of edges to delete, check same for matrix as well
    def update_adjacency_list(self, operation, del_edges=[]):
        """
        Update the adjacency list after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        if operation == 1:
            for i in range(self.E, len(self.edges_list)):
                self.adjacency_list[self.edges_list[i][0]].append(self.edges_list[i][1:-1])
                if self.is_undirected:
                    self.adjacency_list[self.edges_list[i][1]].append([self.edges_list[i][0], self.edges_list[i][2]])
            print(f"\nNew adj_list: {np.array(self.adjacency_list)}. \n Time = O(1)")
        else:
            for i in range(self.E, len(del_edges)):
                self.adjacency_list[del_edges[i][0]].remove(del_edges[i][1])
                if self.is_undirected:
                    self.adjacency_list[del_edges[i][1]].remove(del_edges[i][0])
            print(f"\nNew adj_list: {np.array(self.adjacency_list)}. \n Time = O(V)")
    
    def update_adjacency_matrix(self,operation, del_edges=[]):
        """
        Update the adjacency matrix after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        if operation == 1:
            for i in range(self.E, len(self.edges_list)):
                if self.is_weighted:
                    weight = self.edges_list[i][2]
                else:
                    weight = 1
                self.adjacency_matrix[self.edges_list[i][0]][self.edges_list[i][1]] = weight
                if self.is_undirected:
                    self.adjacency_matrix[self.edges_list[i][1]][self.edges_list[i][0]] =  weight
            print(f"\nNew adjacency_matrix: {np.array(self.adjacency_matrix)}. \n Time = O(1)")
        else:
            for i in range(len(del_edges)):
                self.adjacency_matrix[del_edges[i][0]][del_edges[i][1]] = 0
                self.adjacency_matrix[del_edges[i][1]][del_edges[i][0]] = 0
            print(f"\nNew adjacency_matrix: {np.array(self.adjacency_matrix)}. \n Time = O(1)")

    def update_incidence_matrix(self, operation, del_edges=[]):
        """
        Update the incidence matrix after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        if operation == 1:
            for i in range(self.E, len(self.edges_list)):
                self.incidence_matrix[self.edges_list[i][0]][i] = 1
                if self.is_undirected:
                    self.incidence_matrix[self.edges_list[i][1]][i] = 1
                else:
                    self.incidence_matrix[self.edges_list[i][1]][i] = -1
                
            print(f"\nNew incidence_matrix: {np.array(self.incidence_matrix)}. \n Time = O(1)")
        else:
            for i in range(len(del_edges)):
                edge_to_del = self.edges_list.index(del_edges[i])
                self.incidence_matrix[del_edges[i][0]][edge_to_del] = 0
                self.incidence_matrix[del_edges[i][1]][edge_to_del] = 0
            print(f"\nNew incidence_matrix: {np.array(self.incidence_matrix)}. \n Time = O(E)")
     
    def update_all_views(self, operation, del_edges=[]):
        """
        Update all the views after adding an edge.
        """
        self.update_adjacency_list(operation, del_edges)
        self.update_adjacency_matrix(operation, del_edges)
        self.update_incidence_matrix(operation, del_edges)

class Graph(GraphView):
    def __init__(self, V, E, edges):
        super().__init__(V, E, edges)
        self.is_undirected = True
        self.is_weighted = False
         
    def add_edge(self, edge, weight=None):
        """
        Add an edge to the graph.
        edge: tuple of two vertices
        weight: weight of the edge, if the graph is weighted
        """
        if self.is_weighted:
            if weight is None:
                raise ValueError("Weighted graph needs a weight for the edge")
            edge = (edge, weight)
        self.edges_list.append(edge)
        self.update_all_views(1)
        self.E += 1

    def add_edges(self, edges):
        """
        Add multiple edges to the graph.
        edges: list of tuples of two vertices
        """
        if self.is_weighted:
            if len(edges[0]) == 2:
                raise ValueError("Weighted graph needs weights for the edges")
        self.edges_list.extend(edges)
        self.update_all_views(1)
        self.E += len(edges)
    
    def delete_edges(self, del_edges):
        """
        Delete an edge from the graph.
        edge: tuple of two vertices
        """
        for edge in del_edges:
            if edge not in self.edges_list:
                raise ValueError("Edge not found in the graph")
            self.edges_list.remove(edge)
        self.update_all_views()
        self.E -= len(del_edges)
        
        
g1 = Graph(4, 5, [(0, 1), (1, 2), (2, 3),(3,0),(0,2)])
g1.is_undirected = True
g1.is_weighted = False

g1.add_edge((1,3))
print(g1.adjacency_list)
print(g1.adjacency_matrix)
print(g1.incidence_matrix)
plt.figure(figsize=(8, 6))
G1 = nx.from_edgelist(g1.edges_list)
nx.draw(G1, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15, font_color='black')
plt.title("Graph from Adjacency Matrix")
plt.show()