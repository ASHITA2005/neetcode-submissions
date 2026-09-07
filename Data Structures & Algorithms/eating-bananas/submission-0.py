import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours_needed(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k) if pile//k != 0 else 1
            return hours 
        hi = max(piles)
        lo = 1
        result = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            hours_required = hours_needed(mid)
            if hours_required <= h:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
            
        return result 
                
