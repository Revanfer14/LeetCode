class Solution {
    func decompressRLElist(_ nums: [Int]) -> [Int] {

        let len = nums.count / 2
        var freq = 0
        var val = 0

        var res: [Int] = []

        var x = 0

        for i in stride(from: 0, to: nums.count, by: 2) {
            print(i)
            if i > nums.count {
                break
            } else {
                freq = nums[i]
                val = nums[i+1]

                print("I = \(i) -> Freq \(freq) Val \(val)")

                for j in 0..<freq {
                    res.append(val)
                }
            }
        }
        return res
    }
}