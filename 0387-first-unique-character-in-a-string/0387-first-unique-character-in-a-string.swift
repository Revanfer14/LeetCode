class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var hashMap: [Character: Int] = [:]

        for c in s {
            if let count = hashMap[c] {
                hashMap[c] = count + 1
            } else {
                hashMap[c] = 1
            }
        }

        for (i, n) in s.enumerated() {
            if hashMap[n] == 1 {
                return i
            }
        }

        return -1
    }
}