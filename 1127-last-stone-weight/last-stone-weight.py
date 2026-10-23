import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i] #because heapq is min heap by def

        heapq.heapify(stones)

        while len(stones)>1:
            largest=heapq.heappop(stones)
            next_largest=heapq.heappop(stones)

            if largest!=next_largest:
                heapq.heappush(stones, largest-next_largest)
        
        if len(stones)==1:
            return -heapq.heappop(stones)
        else:
            return 0
        