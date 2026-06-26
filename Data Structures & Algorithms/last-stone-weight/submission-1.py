class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for num in stones:
            heapq.heappush(max_heap,-num)
        while max_heap:
            if len(max_heap) ==1:
                return -max_heap[0]
            else:
                l1 = heapq.heappop(max_heap)
                l2 = heapq.heappop(max_heap)
                if l1==l2:
                    continue
                heapq.heappush(max_heap,l1-l2)
        return 0