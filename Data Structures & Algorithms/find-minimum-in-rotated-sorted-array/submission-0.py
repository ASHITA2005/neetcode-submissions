class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        min_ele = nums[0]
        lo = 0 
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[mid]



