#active recall
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=defaultdict(list) #list is the datatype
        for u,v,time in times:
            graph[u].append((v,time))
        min_times={} #node: dist of the node from the source node
        min_heap=[(0,k)] #(dist of the node from the source node, node)

        while min_heap:
            # time_k_to_i, i = min_heap.pop()
            time_k_to_i, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            min_times[i]=time_k_to_i
            for nei, nei_time in graph[i]: #this is the power of representing a graph as an adjacency list
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_k_to_i+nei_time, nei))
        
        if len(min_times)==n:
            return max(min_times.values()) #keys' values
        else:
            return -1

#TC: O((V+E)*logV)
#SC: O(V+E)