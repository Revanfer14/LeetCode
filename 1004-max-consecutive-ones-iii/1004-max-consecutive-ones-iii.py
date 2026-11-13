class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        n = len(nums)
        max_len = 0

        num_zero = 0

        for r in range(n):
            if nums[r] == 0:
                num_zero += 1

            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1

            w = r-l+1
            max_len = max(max_len, w)

        return max_len