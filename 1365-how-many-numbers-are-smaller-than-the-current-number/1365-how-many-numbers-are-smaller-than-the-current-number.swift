class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        var res: [Int] = []
        let len = nums.count

        for i in 0..<len {
            var counter: Int = 0

            for j in 0..<len {
                if nums[i] > nums[j] {
                    counter += 1
                }
            }

            res.append(counter)
        }

        return res
    }
}