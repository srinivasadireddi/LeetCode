#Active Recall
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val=val
#         self.neighbors=neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node:Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        start= node
        old_to_new={} #HASHMap
        # old_to_new[start]=Node(val=start.val)
        visited=set()
        visited.add(start)
        stack=[]
        stack.append(start)

        while stack:
            node=stack.pop()
            # if node not in visited:
            visited.add(node)
            old_to_new[node]=Node(val=node.val)

            for nei in node.neighbors:
                # if nei is not in visited:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        #dfs done and old_to_new hashmap created
        #now, lets make connections

        for old_node, new_node in old_to_new.items(): 
            for old_nei in old_node.neighbors:
                # new_nei = Node(val=old_nei.val)
                new_nei = old_to_new[old_nei]
                # new_node.neighbhor(new_nei)
                new_node.neighbors.append(new_nei)
        
        return old_to_new[start]
#TC: O(V+E)
#SC: O(V)
            


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None
            
#         start=node
#         stack=[start] #we'll do dfs
#         old_to_new={}
#         visited= set() #redundant (we can identify visited nodes using the dict) but nice to have it
#         visited.add(start)

#         while stack:
#             node=stack.pop()
#             old_to_new[node]=Node(val=node.val)

#             for nei in node.neighbors:
#                 if nei not in visited:
#                     visited.add(nei)
#                     stack.append(nei)
        
#         for old_node, new_node in old_to_new.items():
#             for nei in old_node.neighbors:
#                 new_nei=old_to_new[nei]
#                 new_node.neighbors.append(new_nei)
        
#         return old_to_new[start]
# #TC:O(V+E) #V cuz stack's worst case is V and E cuz we see neighbors
# #SC:O(V)