class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        dictNums = Counter(nums)

        arr = []

        for num in dictNums:
            if dictNums[num] <= 1:
                arr.append(num)

        return arr