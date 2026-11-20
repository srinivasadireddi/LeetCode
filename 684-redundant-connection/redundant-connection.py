class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n= len(edges)
        par = [i for i in range(n+1)]
        rank= [1]*(n+1) #size of a component

        def find(n):
            if n==par[n]:
                return par[n]
            return find(par[n])

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 ==p2:
                return False
            
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
#TC: O(E+V)
#SC: O(V)
            
            


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         root = list(range(len(edges) + 1)) # each node is root of own subtree

#         def find_root(node):
#             if root[node] != node:
#                 root[node] = find_root(root[node]) # set root for node as root of subtree
#             return root[node] # found root of subtree

#         for node1, node2 in edges: 
#             root1, root2 = find_root(node1), find_root(node2)

#             if root1 == root2:
#                 return [node1, node2] # both nodes are already in same subtree
 
#             root[root2] = root1 # found new connection between nodes / subtrees
#             # root[root1] = root2 also works            
#TC: O(E+V)
#SC: O(V)
