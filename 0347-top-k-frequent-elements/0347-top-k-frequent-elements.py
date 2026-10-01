class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numDict = Counter(nums)
        numList = numDict.most_common()

        print(numList)
        result = []

        for i in range(k):
            key = numList[i]
            
            result.append(key[0])

        return result