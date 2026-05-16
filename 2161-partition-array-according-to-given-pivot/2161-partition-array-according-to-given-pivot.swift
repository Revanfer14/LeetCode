class Solution {
    func pivotArray(_ nums: [Int], _ pivot: Int) -> [Int] {
        var left: [Int] = []
        var right: [Int] = []
        var isPivot: [Int] = []

        let res: [Int]

        for i in nums {
            if i == pivot {
                isPivot.append(i)
            } else if i < pivot {
                left.append(i)
            } else {
                right.append(i)
            }
        }

        res = left + isPivot + right
        
        return res
    }
}