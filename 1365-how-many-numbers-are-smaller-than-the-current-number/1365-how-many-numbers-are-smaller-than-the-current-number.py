class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []

        for i in range(len(nums)):
            x = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    x += 1
            
            res.append(x)
        
        return res
