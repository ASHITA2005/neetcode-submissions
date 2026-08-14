class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = [0] * n
        i = 0
        stack = []
        while i < n:
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    num, pos = stack.pop()
                    result[pos] = i - pos
                stack.append((temperatures[i], i))
            i += 1
        return result
                

