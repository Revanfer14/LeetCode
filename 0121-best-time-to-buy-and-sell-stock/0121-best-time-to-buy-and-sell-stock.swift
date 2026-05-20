class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var minPrice = Int.max
        var profit = 0

        for i in prices {
            if i < minPrice {
                minPrice = i
            } else if i - minPrice > profit {
                profit = i - minPrice
            }
        }

        return profit
    }
}