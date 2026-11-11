class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        arr = []

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        for i in range(len(stones)):
            heapq.heappush(arr, stones[i])

        while len(arr) > 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)

            heapq.heappush(arr, x-y)

        return -arr[0]