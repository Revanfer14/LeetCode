class Solution {
    func totalWaviness(_ num1: Int, _ num2: Int) -> Int {
        var res: Int = 0

        for i in num1...num2 {
            let tc = String(i).compactMap { num in 
                Int(String(num))
            }

            for j in 1..<tc.count {

                if j + 1 == tc.count {
                    break
                }

                if tc[j-1] > tc[j] && tc[j+1] > tc[j] || tc[j-1] < tc[j] && tc[j+1] < tc[j] {
                    res += 1
                }
            }
        }

        return res
    }
}