class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        result = []

        for n in range (len(nums)):
            if sorted_nums[n] == target:
                result.append(n)

        return result