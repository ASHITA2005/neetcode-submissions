class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stack = []
        n = len(prices)
        i = 0
        while i < n:
            while stack and stack[-1] > prices[i]:
                stack.pop()
            stack.append(prices[i])
            i += 1
            profit = max(profit, stack[-1]- stack[0])
        return profit