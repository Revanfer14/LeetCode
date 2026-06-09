class Solution {
    func maxTotalValue(_ nums: [Int], _ k: Int) -> Int {
        guard let x = nums.minAndMax() else {
            return 0
        }

        return (x.max - x.min) * k
    }
}