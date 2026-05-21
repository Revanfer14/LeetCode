class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        let setNums = Set(nums)

        let newArr = Array(setNums).sorted()

        nums = newArr

        return nums.count
    }
}