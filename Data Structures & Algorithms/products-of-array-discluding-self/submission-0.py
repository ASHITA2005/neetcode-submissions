class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]
        right_prod = [1]
        j = 1
        for i in range(len(nums)):
            left_prod.append(left_prod[j-1] * nums[i])
            j += 1
        j = 1
        for i in range(len(nums)-1, -1, -1):
            right_prod.append(right_prod[j-1] * nums[i])
            j+= 1
        # print(left_prod)
        # print(right_prod)
        result = [1] * len(nums)
        j = 1
        for i in range(len(nums)):
            result[i] = left_prod[j-1] * right_prod[-(j + 1)]
            j += 1
            
        return result