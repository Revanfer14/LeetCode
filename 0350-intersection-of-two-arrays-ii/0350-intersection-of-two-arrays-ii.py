class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        x = Counter(nums1)
        result = []
        
        for num in nums2:
            if num in x and x[num] > 0:
                result.append(num)
                x[num] -= 1

        return result