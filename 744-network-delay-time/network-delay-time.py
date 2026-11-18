# class Solution:
#     def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        adj = [[] for i in range(n + 1)]

        for u, v, w in times:
            adj[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:

            dis, node = heappop(heap)

            if dis > dist[node]:
                continue

            for neigh, weight in adj[node]:

                new_dist = dis + weight

                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    heappush(heap, (new_dist, neigh))

        ans = max(dist[1:])

        return ans if ans != float("inf") else -1