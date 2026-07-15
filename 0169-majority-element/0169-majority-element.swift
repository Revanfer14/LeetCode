class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var n = nums.sorted()
        var len = n.count
        return n[len/2]
    }
}