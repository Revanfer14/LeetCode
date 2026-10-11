class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        numLen = len(nums)
        res = 0

        for i in range(numLen):
            if numLen % (i+1) == 0:
                helper = nums[i] * nums[i]
                res += helper
        
        return res