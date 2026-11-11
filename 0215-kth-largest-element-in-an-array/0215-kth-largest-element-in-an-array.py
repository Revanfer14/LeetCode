class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int: 
        arr = []

        for n in nums:
            if len(arr) < k:
                heapq.heappush(arr, n)
            else:
                if arr[0] < n:
                    heapq.heappop(arr)
                    heapq.heappush(arr, n)

        return arr[0]