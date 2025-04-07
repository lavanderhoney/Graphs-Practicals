def generate_power_set(iterable):
    """
    Generate all non-empty subsets of the input iterable.
    This implementation uses bit manipulation to generate subsets.
    """
    items = list(iterable)
    n = len(items)
    subsets = []
    # Loop from 1 to 2^n - 1 (excluding the empty set)
    for i in range(1, 1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j): #left shift 1 by j bits
                subset.append(items[j])
        subsets.append(subset)
    return subsets

def build_graph(vertices, edges):
    """
    Build an undirected graph represented as an adjacency list.
    """
    graph = {v: set() for v in vertices}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return graph

def is_connected(vertices, edges):
    """
    Check if the graph defined by the list of vertices and the given list of edges is connected.
    Uses Depth-First Search (DFS).
    """
    if not vertices:
        return True

    graph = build_graph(vertices, edges)
    start = vertices[0]
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Add unvisited neighbors to the stack
            stack.extend(graph[node] - visited)
            
    return len(visited) == len(vertices)

def find_cut_sets(vertices, edges):
    """
    Find all cut-sets of the graph by generating the power set of edges.
    A cut-set is a set of edges whose removal disconnects the graph.
    """
    all_cut_sets = []
    # Generate all non-empty subsets of the edge list
    all_subsets = generate_power_set(edges)
    
    for subset in all_subsets:
        # Construct the list of remaining edges after removing the current subset
        remaining_edges = [edge for edge in edges if edge not in subset]
        if not is_connected(vertices, remaining_edges):
            all_cut_sets.append(set(subset))
    
    return all_cut_sets
def find_articulation_points(vertices, edges):
    """
    Find all articulation points in the graph.
    A vertex is an articulation point if its removal disconnects the graph.
    """
    articulation_points = []
    
    # Assume the original graph is connected.
    for v in vertices:
        # Remove vertex v from the list of vertices.
        remaining_vertices = [u for u in vertices if u != v]
        # Remove edges incident to vertex v.
        remaining_edges = [ (u, w) for (u, w) in edges if u != v and w != v ]
        
        # Check connectivity of the remaining graph.
        if remaining_vertices and not is_connected(remaining_vertices, remaining_edges):
            articulation_points.append(v)
            
    return articulation_points

if __name__ == "__main__":
   
    vertices = ['A', 'B', 'C', 'D','E']
    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('D', 'A'),
        ('A', 'C'),
        ('B', 'D'),
        ('A', 'E') 
    ]
    
    cut_sets = find_cut_sets(vertices, edges)
    print("Cut-sets of the graph:")
    for i, cs in enumerate(cut_sets, 1):
        print(f"Cut-set {i}: {cs}")
    articulation_pts = find_articulation_points(vertices, edges)
    print("Articulation Points:", articulation_pts)
