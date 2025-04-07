import random
import copy

def karger_min_cut(graph, iterations=100):
    """
    Runs Karger's randomized min-cut algorithm on the input graph for a given number of iterations.
    
    Parameters:
        graph (dict): An undirected graph represented as a dictionary where each key is a vertex 
                      and its value is a list of adjacent vertices.
        iterations (int): The number of times the algorithm is run.
    
    Returns:
        tuple: (min_cut_value, best_contracted_graph) where best_contracted_graph is the 
               contracted graph (with two vertices) that produced the min cut.
    """
    min_cut = float('inf')
    best_cut_graph = None

    for i in range(iterations):
        local_graph = copy.deepcopy(graph)
        
        while len(local_graph) > 2:
            u = random.choice(list(local_graph.keys()))
            v = random.choice(local_graph[u])
            
            # Merge v into u by extending u's list with v's adjacent vertices.
            local_graph[u].extend(local_graph[v])
            
            del local_graph[v]
            
            # Replace all occurrences of v with u in the graph.
            for vertex in local_graph:
                local_graph[vertex] = [u if x == v else x for x in local_graph[vertex]]
            
            # Remove self-loops from u's list.
            local_graph[u] = [x for x in local_graph[u] if x != u]
        
        # At this point, the graph has two vertices. The cut value is the number of edges 
        # between these two remaining vertices.
        cut_value = len(list(local_graph.values())[0])
        if cut_value < min_cut:
            min_cut = cut_value
            best_cut_graph = local_graph

    return min_cut, best_cut_graph

if __name__ == "__main__":
    graph = {
        '1': ['2', '3', '4'],
        '2': ['1', '3', '4'],
        '3': ['1', '2', '4'],
        '4': ['1', '2', '3']
    }
    
    iterations = 200  
    min_cut, contracted_graph = karger_min_cut(graph, iterations)
    print("Minimum cut:", min_cut)
