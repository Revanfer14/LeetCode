class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        x = {}

        for i, val in enumerate(nums1):
            if val in nums2:
                x[i] = val
            
        result = []

        for num in x.values():
            result.append(num)

        return list(set(result))