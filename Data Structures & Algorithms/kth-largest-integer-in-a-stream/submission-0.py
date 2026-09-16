from heapq import heappush, heappop, heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.n = []
        for i in range(len(nums)):
            heappush(self.n, nums[i])
            if len(self.n) > self.k:
                heappop(self.n)

        

    def add(self, val: int) -> int:
        heappush(self.n, val)
        if len(self.n) > self.k:
            heappop(self.n)
        return self.n[0]
        
