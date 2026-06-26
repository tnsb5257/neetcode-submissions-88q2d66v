import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.KLargestEls = nums
        heapq.heapify(self.KLargestEls)
        while len(self.KLargestEls) > k:
            heapq.heappop(self.KLargestEls)

    def add(self, val: int) -> int:
        if not self.KLargestEls:
            heapq.heappush(self.KLargestEls,val)
            return val
        else:
            heapq.heappush(self.KLargestEls,val)
            if len(self.KLargestEls) > self.k:
                heapq.heappop(self.KLargestEls)
            return self.KLargestEls[0]