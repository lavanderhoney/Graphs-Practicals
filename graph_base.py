import numpy as np
import networkx as nx
from networkx.linalg import graphmatrix
from matplotlib import pyplot as plt


class GraphView():
    def __init__(self, V, E, edges, is_undirected=True, is_weighted=False, is_labelled=False):
        """
        Initialize the graph view.
        V: number of vertices
        E: number of edges
        edges: list of edges
        is_undirected: (default=True) True if the graph is undirected, False otherwise
        is_weighted: (default=False) True if the graph is weighted, False otherwise
        is_labelled: (default=False) True if the graph is labelled, False otherwise
        """
        self.V = V  # number of vertices
        self.E = E  # number of edges
        self.edges_list = edges  # list of edges
        self.last_el_ptr = 0  # pointer to the last element in the edge list
        self.is_undirected = is_undirected  # True if the graph is undirected
        self.is_weighted = is_weighted  # True if the graph is weighted
        self.is_labelled = is_labelled
        self.adjacency_list = [[] for _ in range(self.V)]
        self.adjacency_matrix = [
            [0 for _ in range(self.V)] for __ in range(self.V)]
        self.incidence_matrix = [[] for __ in range(self.V)]
        self.update_all_views(1)
        self.last_el_ptr += self.E

    def print_adjacency_list(self):
        print("Adjacency List:")
        for i in range(self.V):
            print(f"{i}: {self.adjacency_list[i]}")

    def print_adjacency_matrix(self):
        print("Adjacency Matrix:")
        print(np.array(self.adjacency_matrix))

    def print_incidence_matrix(self):
        print("Incidence Matrix:")
        print(np.array(self.incidence_matrix))
    # provide lists of edges to delete, check same for matrix as well

    def update_adjacency_list(self, operation, del_edges=[]):
        """
        Update the adjacency list after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        if operation == 1:
            # this for loop goes from the last(previous) edge added to the end of the new extended edge_list
            weight = 1
            for i in range(self.last_el_ptr, len(self.edges_list)):
                if self.is_weighted or self.is_labelled:
                    weight = self.edges_list[i][2] #if labelled, weight is actually the label
                self.adjacency_list[self.edges_list[i][0]].append(
                    (self.edges_list[i][1], weight))
                if self.is_undirected:
                    self.adjacency_list[self.edges_list[i][1]].append(
                        (self.edges_list[i][0], weight))
            # print(f"\nNew adj_list: {self.print_adjacency_list()}. \n Time = O(1)") #make display function to print properly
        else:
            for i in range(self.E, len(del_edges)):
                self.adjacency_list[del_edges[i][0]].remove(del_edges[i][1])
                if self.is_undirected:
                    self.adjacency_list[del_edges[i]
                                        [1]].remove(del_edges[i][0])
            # print(f"\nNew adj_list: {self.print_adjacency_list()}. \n Time = O(V)")

    def update_adjacency_matrix(self, operation, del_edges=[]):
        """
        Update the adjacency matrix after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        if operation == 1:
            for i in range(self.last_el_ptr, len(self.edges_list)):
                if self.is_weighted:
                    weight = self.edges_list[i][2]
                else:
                    weight = 1
                self.adjacency_matrix[self.edges_list[i]
                                      [0]][self.edges_list[i][1]] = weight
                if self.is_undirected:
                    self.adjacency_matrix[self.edges_list[i]
                                          [1]][self.edges_list[i][0]] = weight
            # print(f"\nNew adjacency_matrix: {self.print_adjacency_matrix()}. \n Time = O(1)")
        else:
            for i in range(len(del_edges)):
                self.adjacency_matrix[del_edges[i][0]][del_edges[i][1]] = 0
                self.adjacency_matrix[del_edges[i][1]][del_edges[i][0]] = 0
            # print(f"\nNew adjacency_matrix: {self.print_adjacency_matrix()}. \n Time = O(1)")

    def update_incidence_matrix(self, operation, del_edges=[]):
        """
        Update the incidence matrix after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        self.incidence_matrix = [
            [0 for _ in range(len(self.edges_list))] for __ in range(self.V)]

        if operation == 1:
            for i in range(len(self.edges_list)):
                self.incidence_matrix[self.edges_list[i][0]][i] = 1
                self.incidence_matrix[self.edges_list[i][1]][i] = 1
            # print(f"\nNew incidence_matrix: {self.print_incidence_matrix()}. \n Time = O(V*E)")
        else:
            for i in range(len(del_edges)):
                edge_to_del = self.edges_list.index(del_edges[i])
                self.incidence_matrix[del_edges[i][0]][edge_to_del] = 0
                self.incidence_matrix[del_edges[i][1]][edge_to_del] = 0
            # print(f"\nNew incidence_matrix: {self.print_incidence_matrix()}. \n Time = O(E)")

    def update_all_views(self, operation, del_edges=[]):
        """
        Sorts the edges list and then Update all the views after adding an edge.
        operation: 1 for adding an edge, 0 for deleting an edge
        """
        self.edges_list.sort(
            key=lambda x: x[0])  # sort the edges list: O(ElogE)
        self.update_adjacency_list(operation, del_edges)
        self.update_adjacency_matrix(operation, del_edges)
        self.update_incidence_matrix(operation, del_edges)


class Graph(GraphView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, edge):
        """
        Add an edge to the graph.
        edge: tuple of two vertices
        weight: weight of the edge, if the graph is weighted
        """
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
        self.update_all_views(1, del_edges)
        self.E -= len(del_edges)

    def print_graph_nx(self):
        if self.is_weighted:
            edges = [(edge[0], edge[1]) for edge in self.edges_list]
        elif self.is_labelled:
            edges = []
            edge_labels = dict()
            for edge in self.edges_list:
                edges.append((edge[0], edge[1]))
                edge_labels[(edge[0], edge[1])] = edge[2]
        else:
            edges = self.edges_list

        G = nx.MultiGraph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(G, pos, with_labels=True, node_color='skyblue',
                node_size=2000, edge_color='gray', font_size=15, font_color='black',
                connectionstyle='arc3, rad = 0.1',
                )
        if self.is_labelled:
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels=edge_labels,
                font_color="red",
            )
        plt.axis("off")
        plt.title("Graph from Adjacency Matrix")
        plt.show()


if __name__ == "__main__":
    # Example usage
    g1 = Graph(4, 6, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2),
               (1, 3)], is_undirected=True, is_weighted=False)
    g1.print_graph_nx()

    g1.add_edge((1, 3))

    g1.print_graph_nx()

    g1.delete_edges([(1, 3)])

    g1.print_graph_nx()
