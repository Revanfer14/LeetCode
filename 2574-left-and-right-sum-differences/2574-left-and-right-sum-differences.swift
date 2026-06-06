class Solution {
    func leftRightDifference(_ nums: [Int]) -> [Int] {
        var len = nums.count - 1

        var left: [Int] = [0]
        var right: [Int] = [0]
        var res: [Int] = []

        if len == 0 {
            res.append(0)
            return res
        }

        var curr: Int = 0

        for i in 0..<len {
            if i == len {
                break
            }

            curr = left[i] + nums[i]
            left.append(curr)
        }

        var reversed = Array(nums.reversed())

        for i in 0..<len {
            if i == len {
                break
            }

            curr = right[i] + reversed[i]
            right.append(curr)
        }

        var newRight = right.sorted {
            $0 > $1
        }
        
        for i in 0..<nums.count {
            res.append(abs(left[i] - newRight[i]))
        }

        print("Left: \(left)")
        print("Right: \(newRight)")

        return res
    }
}