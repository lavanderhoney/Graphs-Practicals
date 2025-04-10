"""
Approach:
1. Construct the graph from given ticket lists.
    -> create mapping for airport code to int index (starting from 0)
    -> then use that and create the edge list, and make the graph

2. Find the Eulerian path in the graph.
    -> start from JFK
    -> count the number of edges visited, by putting them in a visited set
    -> if the edge is not visited, then visit it and add it to the path
    -> if the edge is visited, then backtrack and add it to the path
    -> if length of visited edges is equal to total edges, then return the path
    
"""

from collections import defaultdict
from typing import List

import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build adjacency list and track degree of each node
        adj = collections.defaultdict(list)
        degree = collections.defaultdict(int)  # Track the degree of each node

        for source, dest in tickets:
            adj[source].append(dest)
            degree[source] += 1
            degree[dest] += 1  # Increase degree for both nodes

        # Step 2: Sort adjacency list for lexicographical order traversal
        for key in adj:
            adj[key].sort()

        # Step 3: Explicitly check if all nodes have even degree
        odd_cntr=0
        for node in degree:
            if degree[node] % 2 != 0:  # Check if any node has an odd degree
                odd_cntr+=1
        if odd_cntr>2:
            print("Not valid eularian circuit")
            return []
        
        itinerary = []

        def dfs(at):
            while adj[at]:
                next_dest = adj[at].pop(0)
                dfs(next_dest)
            itinerary.append(at)

        dfs("JFK")
        return itinerary[::-1]

itenary = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
ans = itenary.findItinerary(tickets)
print(ans)
