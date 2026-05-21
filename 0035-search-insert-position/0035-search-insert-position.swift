class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var res = 0

        for i in 0..<nums.count {
            if nums[i] == target {
                res = i
                break
            } else if target > nums[i] {
                res = i+1
            }
        }

        return res
    }
}