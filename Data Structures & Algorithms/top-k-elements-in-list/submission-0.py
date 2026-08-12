from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict(Counter(nums))
        frequency = []
        for val in freq:
            frequency.append((val, freq[val]))
        freq = sorted(frequency, key = lambda x: -x[1])
        result = [val for val, count in freq[:k]]
        return result
        
        