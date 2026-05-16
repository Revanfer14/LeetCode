class Solution {
    func alternatingSum(_ nums: [Int]) -> Int {
        let len = nums.count

        var res = 0
        for i in 0..<len {
            if i % 2 == 0 {
                res += nums[i]
            } else {
                res -= nums[i]
            }
        }

        return res
    }
}