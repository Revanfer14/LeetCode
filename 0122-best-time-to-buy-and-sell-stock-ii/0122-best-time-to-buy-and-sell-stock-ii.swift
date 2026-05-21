class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var profit = 0

        for i in 1..<prices.count {
            if prices[i] > prices[i-1] {
                print("Profit \(profit)")
                profit += prices[i] - prices[i-1]
            }
        }

        return profit
    }
}