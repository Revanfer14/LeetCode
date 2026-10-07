class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        sortNum = nums.sort()

        gap = 0

        for i in range(0, len(nums)):
            if nums[i] - nums[i-1] > gap:
                gap = nums[i] - nums[i-1]
        
        return gap
