class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dict = {}
        flag = False

        for i, val in enumerate(nums):
            if val in dict:
                y = dict[val]
                if abs(i - y) <= k:
                    flag = True
                    break
            
            dict[val] = i

        return flag