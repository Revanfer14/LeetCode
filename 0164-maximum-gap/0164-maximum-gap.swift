class Solution {
    func maximumGap(_ nums: [Int]) -> Int {
        if nums.count < 2 {
            return 0
        }

        var gap = 0

        var n = nums.sorted()

        for i in 1..<n.count {
            if gap < (n[i] - n[i-1]) {
                gap = n[i] - n[i-1]
            }
        }

        return gap
    }
}