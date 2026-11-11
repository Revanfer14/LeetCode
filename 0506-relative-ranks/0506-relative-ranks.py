class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        arr = []

        for s in range(len(score)):
            heapq.heappush(arr, (-score[s], s))

        res = [""] * len(score)

        print(arr)

        rank = 1

        while arr:
            num, i = heapq.heappop(arr)
            
            if rank == 1:
                res[i] = "Gold Medal"
            elif rank == 2:
                res[i] = "Silver Medal"
            elif rank == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank)
            
            rank += 1

        return res
