# #three methods
# #mtd 1: DFS w recursion

# class Solution:
#     def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
#             #base case
#             if (source==destination):
#                 return True
            
#             #create a dictionary for graph
#             graph= defaultdict(list)

#             for u,v in edges:
#                 graph[u].append(v)
#                 graph[v].append(u)
            
#             #avoid infinite loop
#             seen= set()
#             seen.add(source)

#             #helper function
#             def dfs(i):
#                 if i==destination:
#                     return True
#                 for nei_node in graph[i]:
#                     if nei_node not in seen:
#                         seen.add(nei_node)
#                         if dfs(nei_node):
#                             return True
#                 return False
            
#             return dfs(source)

#mtd2: dfs with stack
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
            #base case
            if (source==destination):
                return True
            
            #create a dictionary for graph
            graph= defaultdict(list)

            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            #avoid infinite loop
            seen= set()
            seen.add(source)    

            #stack
            stack=[source]
            while stack:
                node=stack.pop() #pops most recent node
                if node==destination:
                    return True
                for nei_node in graph[node]:
                    if nei_node not in seen:
                        seen.add(nei_node)
                        stack.append(nei_node)
            return False    

