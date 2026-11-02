class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        size = len(nums)

        mid = size // 2

        sorted_nums = sorted(nums)
        res = 0

        for n in sorted_nums:
            res += abs(n - sorted_nums[mid])
        
        return res
