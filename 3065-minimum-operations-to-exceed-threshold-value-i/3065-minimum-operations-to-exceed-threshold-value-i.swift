class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {

        var result = 0

        for i in nums {
            if i < k {
                result += 1
            }
        }

        return result
    }
}