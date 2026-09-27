class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for i, value in enumerate(nums):
            x = target - value

            if x in dict:
                y = dict[x]
                return y, i

            dict[value] = i

        return []