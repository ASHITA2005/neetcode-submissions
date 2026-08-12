class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stack = []
        nums = sorted(nums)
        max_len = 0
        i = 0
        #print(nums)
        while i < len(nums):
            if not stack:
                stack.append(nums[i])
            while stack and stack[-1] + 1 != nums[i]:
                stack.pop()
            stack.append(nums[i])   
            i += 1
            max_len = max(max_len, len(stack))
            #print(stack)
        return max_len


            