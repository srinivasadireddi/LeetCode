"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start=node
        stack=[start] #we'll do dfs
        old_to_new={}
        visited= set() #redundant (we can identify visited nodes using the dict) but nice to have it
        visited.add(start)

        while stack:
            node=stack.pop()
            old_to_new[node]=Node(val=node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        for old_node, new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_nei=old_to_new[nei]
                new_node.neighbors.append(new_nei)
        
        return old_to_new[start]
#TC:O(V+E) #V cuz stack's worst case is V and E cuz we see neighbors
#SC:O(V)