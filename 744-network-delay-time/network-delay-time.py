# class Solution:
#     def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

#revised
#Greg's solution
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra's Algorithm
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))
        
        min_times = {}
        min_heap = [(0, k)] # (distance from source to node, node)

        while min_heap:
            time_k_to_i, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            
            min_times[i] = time_k_to_i
            for nei, nei_time in graph[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))
        
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
        # Time: O((V + E) log (V)) 
        # Space: O(V + E)

# from heapq import heappop, heappush

# class Solution:
#     def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

#         adj = [[] for i in range(n + 1)]

#         for u, v, w in times:
#             adj[u].append((v, w))

#         dist = [float("inf")] * (n + 1)
#         dist[k] = 0

#         heap = [(0, k)]

#         while heap:

#             dis, node = heappop(heap)

#             if dis > dist[node]:
#                 continue

#             for neigh, weight in adj[node]:

#                 new_dist = dis + weight

#                 if new_dist < dist[neigh]:
#                     dist[neigh] = new_dist
#                     heappush(heap, (new_dist, neigh))

#         ans = max(dist[1:])

#         return ans if ans != float("inf") else -1

#Solution 2
# class Solution:
#     def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
#         # lets create adjacency list as 1 -> (2, 1) : A -> (B, W)

#         edges = {i: [] for i in range(1, n+1)}
#         for i in times:
#             edges[i[0]].append((i[1], i[2]))
        
#         heap = [(0,k)]
#         # keep track of visited nodes
#         visited = set()
#         delays = 0
#         # heap helps with getting the nearest node
#         while heap:
#             time, node = heapq.heappop(heap)
#             if node in visited:
#                 continue
#             visited.add(node)
#             # because we are tracking max time taken by signal to reach
#             delays = max(time, delays)
#             for nei in edges[node]:
#                 if nei not in visited:
#                     heapq.heappush(heap, (time+nei[1], nei[0]))

#         return delays if len(visited) == n else -1