class Solution {
    func isPalindrome(_ s: String) -> Bool {
        var char = Array(s.lowercased().filter { x in
            x.isLetter || x.isNumber
        })

        var left = 0
        var right = char.count - 1

        let len = char.count / 2

        for i in 0..<len {
            if char[left] != char[right] {
                return false
            }

            left = left + 1
            right = right - 1
        }

        return true
    }
}