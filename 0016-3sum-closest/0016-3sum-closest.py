class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        x = len(nums)

        closest = float('inf')

        for i in range(x):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, x-1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                
                if cur_sum == target:
                    return cur_sum
                elif cur_sum > target:
                    r -= 1
                else:
                    l += 1

        return closest
