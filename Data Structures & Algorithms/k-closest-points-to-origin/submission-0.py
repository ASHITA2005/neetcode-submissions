from heapq import heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x, y = point
            distance = x**2 + y**2
            heappush(h, (distance, (x,y)))
        result = []
        for _ in range(k):
            distance, point = heappop(h)
            result.append(point)
        return result
            
