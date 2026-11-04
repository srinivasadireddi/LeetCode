# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = [False] * numCourses
        in_recursion = [False] * numCourses

        adj = [[] for _ in range(numCourses)]

        for v, u in prerequisites:
            adj[u].append(v)

        def dfs(u):
            visited[u] = True
            in_recursion[u] = True

            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True

                elif in_recursion[v]:
                    return True

            in_recursion[u] = False
            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False

        return True

#TC: