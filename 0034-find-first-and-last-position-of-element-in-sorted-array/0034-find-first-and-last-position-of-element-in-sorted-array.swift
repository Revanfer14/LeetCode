class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        var res: [Int] = []

        var firstIdx = nums.firstIndex(of: target) ?? -1
        var lastIdx = nums.lastIndex(of: target) ?? -1

        res += [firstIdx, lastIdx]

        return res
    }
}