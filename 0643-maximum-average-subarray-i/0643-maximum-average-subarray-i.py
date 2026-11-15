class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        n = len(nums)
        curr = sum(nums[:k])

        max_sum = curr

        for r in range(k, n):
            
            curr = curr - nums[l] + nums[r]
            l += 1
            
            max_sum = max(max_sum, curr)

        return max_sum / k