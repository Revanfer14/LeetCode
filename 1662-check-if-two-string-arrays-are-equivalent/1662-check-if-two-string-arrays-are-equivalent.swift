class Solution {
    func arrayStringsAreEqual(_ word1: [String], _ word2: [String]) -> Bool {
        var a = ""
        var b = ""

        for i in 0..<word1.count {
            a += word1[i]
        }
        for i in 0..<word2.count {
            b += word2[i]
        }

        if a == b {
            return true
        } else {
            return false
        }
    }
}