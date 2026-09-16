from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #print(stones)
        stones = [-stone for stone in stones]
        heapify(stones)
        h = stones
        stone1 = 0
        while True:
            #print(h)
            if h:
                stone1 = heappop(h)
            else:
                break
            if h:
                stone2 = heappop(h)
            else:
                break

            if stone1 == stone2 :
                if not h:
                    return 0
                continue
            else:
                final_stone = abs(stone1) - abs(stone2) if stone1 < stone2 else abs(stone2) - abs(stone1)
                heappush(h, -final_stone)
        return -stone1 if stone1 else 0
