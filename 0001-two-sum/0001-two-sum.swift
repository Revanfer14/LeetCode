class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var seen: [Int: Int] = [:]

        for (i, n) in nums.enumerated() {
            let complement = target - n
            print(complement)

            // 2:0 , 7:1
            
            if let j = seen[complement] {
                return [j, i]
            }

            seen[n] = i

            
        }

        return []
    }
}