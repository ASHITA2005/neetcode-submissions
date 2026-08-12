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
                max_len = max(max_len, len(stack))
            elif stack[-1] + 1 == nums[i]:
                stack.append(nums[i])
                max_len = max(max_len, len(stack))
            else:
                while stack and stack[-1] + 1 != nums[i]:
                    stack.pop()
                stack.append(nums[i])
                max_len = max(max_len, len(stack))
                
            i += 1
            #print(stack)
        return max_len


            