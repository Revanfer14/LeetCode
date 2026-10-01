class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numDict = Counter(nums)
        numList = numDict.most_common()

        result = []

        for i in range(k):
            val = numList[i]
            
            result.append(val[0])

        return result