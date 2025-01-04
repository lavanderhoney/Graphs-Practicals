import numpy as np

def store_graph(v, e, edges):
    adj_mat = [[0 for i in range(v)] for j in range(v)]
    for i in range(e):
        adj_mat[edges[i][0]][edges[i][1]] = 1
        adj_mat[edges[i][1]][edges[i][0]] = 1
    print(f"\nAdjacency matrix: \n {np.array(adj_mat)}")
    print("Memory used by adj_mat, O(V*V): ", v*v)

    adj_list = [[] for i in range(v)]
    #undirected graph
    for i in range(e):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
    print(f" \nAdjacency list: \n {np.array(adj_list)}")
    print("Memory used by adj_list, O(V + 2*E): ", v+2*e)

    incidence_mat = [[0 for _ in range(e)] for __ in range(v)]
    for i in range(e):
        incidence_mat[edges[i][0]][i] = 1
        incidence_mat[edges[i][1]][i] = 1
    print(f"\n Incidence matrix: \n {np.array(incidence_mat)}")
    print("Memory used by inc_mat, O(V*E): ", v*e)
    return [adj_mat, adj_list, incidence_mat]

def add_edge(v, e, edges, graph_representations):
    adj_mat = graph_representations[0]
    for i in range(e, e+e_add):
        adj_mat[edges[i][0]][edges[i][1]] = 1
        adj_mat[edges[i][1]][edges[i][0]] = 1
    print(f"\nNew adj_mat: {np.array(adj_mat)}. \n Time = O(1)")

    adj_list = graph_representations[1]
    for i in range(e, e+e_add):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
    print(f"\nNew adj_list: {np.array(adj_list)}. \n Time = O(1)")

    incidence_mat = graph_representations[2]
    for i in range(e, e+e_add):
        incidence_mat[edges[i][0]][i] = 1
        incidence_mat[edges[i][1]][i] = 1
    print(f"\nNew incidence_mat: {np.array(incidence_mat)}. \n Time = O(1)")

    return [adj_mat, adj_list, incidence_mat]

def del_edges(v, e, edges, edges_del, representations):
    adj_mat = representations[0]
    for i in range(len(edges_del)):
        adj_mat[edges_del[i][0]][edges_del[i][1]] = 0
        adj_mat[edges_del[i][1]][edges_del[i][0]] = 0
    print(f"\nNew adj_mat: {np.array(adj_mat)}. \n Time = O(1)")

    adj_list = representations[1]
    for i in range(len(edges_del)):
        adj_list[edges_del[i][0]].remove(edges_del[i][1]) #remove() takes linear time
        adj_list[edges_del[i][1]].remove(edges_del[i][0])
    print(f"\nNew adj_list: {np.array(adj_list)}. \n Time = O(V)")
    
    incidence_mat = representations[2]
    for i in range(len(edges_del)):
        edge_to_del = edges.index(edges_del[i]) #index() takes linear time
        incidence_mat[edges_del[i][0]][edge_to_del] = 0
        incidence_mat[edges_del[i][1]][edge_to_del] = 0
    print(f"\nNew incidence_mat: {np.array(incidence_mat)}. \n Time = O(E)")

v = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))
print("Enter edges: ")
edges =[]
for i in range(e):
    edges.append(list(map(int, input().split())))
print(edges)
representations = store_graph(v, e, edges)

e_add = int(input("Enter number of edges to add: "))
edges_add =[]
print("Enter edges to add: ")
for i in range(e_add):
    edges_add.append(list(map(int, input().split())))
edges.extend(edges_add)

print("Performing addition of edges using all three representations:")
added_representations = add_edge(v, e, edges, representations)

print("Performing deletion of edges using all three representations: ")
e_del = int(input("Enter number of edges to delete: "))
edges_del =[]
print("Enter edges to delete: ")
for i in range(e_del):
    edges_del.append(list(map(int, input().split())))
del_edges(v, e, edges, edges_del, added_representations)