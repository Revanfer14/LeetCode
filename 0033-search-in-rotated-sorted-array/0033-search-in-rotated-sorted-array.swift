class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var res = 0

        for i in 0..<nums.count {
            if target == nums[i] {
                res = i
                break
            }
            res = -1
        }

        return res
    }
}