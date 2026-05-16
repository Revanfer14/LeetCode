class Solution {
    func recoverOrder(_ order: [Int], _ friends: [Int]) -> [Int] {
        let len = order.count
        let len2 = friends.count

        var res: [Int] = []

        for i in 0..<len {
            for j in 0..<len2 {
                if order[i] == friends[j] {
                    res.append(order[i])                               
                    break   
                }
            }
        }

        return res
    }
}