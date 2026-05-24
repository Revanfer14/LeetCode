class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var res = nums.count

        for i in 0..<nums.count {
            print("res before = \(res) | i = \(i) | nums = \(nums[i])")
            res += i - nums[i]
            print("res after = \(res)")
        }

        return res
    }
}