class Solution {
    func truncateSentence(_ s: String, _ k: Int) -> String {
        let textSplit = s.split(separator: " ")

        var res: String = ""

        for i in 0..<k {
            res += textSplit[i] + " "
        }

        return res.trimmingCharacters(in: .whitespaces)
    }
}