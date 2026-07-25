class Solution {
    func maxProduct(_ n: Int) -> Int {
        let arr = String(n).compactMap { x in 
            Int(String(x))
        }.sorted()

        let len = arr.count

        return arr[len-1] * arr[len-2]
    }
}