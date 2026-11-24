class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2

        nums.sort()

        n = len(nums)

        if n % 2 != 0:
            i = n // 2
            return nums[i]
        else:
            i = n // 2
            return (nums[i] + nums[i-1]) / 2