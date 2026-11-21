class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        arr = []

        for x in nums:
            if len(arr) < k:
                heapq.heappush(arr, x)
            else:
                if arr[0] < x:
                    heapq.heappop(arr)
                    heapq.heappush(arr, x)

        return arr[0]