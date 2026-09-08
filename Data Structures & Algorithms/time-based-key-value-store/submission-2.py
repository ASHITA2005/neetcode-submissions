from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))
        #print(self.hash_map)

    def get(self, key: str, timestamp: int) -> str:
        possible_values = self.hash_map[key]
        lo = 0
        hi = len(possible_values) - 1
        #print(possible_values)
        if not possible_values or possible_values[lo][0] > timestamp:
            return ""
        res = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if possible_values[mid][0] <=  timestamp:
                res = possible_values[mid][1] 
                lo = mid + 1
            else:
                hi = mid - 1
        return res
        
        
