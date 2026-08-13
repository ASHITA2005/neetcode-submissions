class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0, len(nums)):
            #print(f'i : {i} and a[i] = {nums[i]}')
            target  = -nums[i]
            hash_map = {}
            for j in range(i+1, len(nums)):
                if target-nums[j] in hash_map:
                    #print(f'j : {j} and a[j] = {nums[j]}')
                    sol = sorted([nums[i], target-nums[j], nums[j]])
                    if sol not in result:
                        result.append(sol)
                    #print(result)
                else:
                    hash_map[nums[j]] = j
        return result

