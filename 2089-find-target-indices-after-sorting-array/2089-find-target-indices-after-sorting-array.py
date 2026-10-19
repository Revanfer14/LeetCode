class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []

        for n in range (len(nums)):
            if nums[n] == target:
                result.append(n)

        return result