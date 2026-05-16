class Solution {
    func mostWordsFound(_ sentences: [String]) -> Int {
        let nums = sentences.count

        var count = 0

        for i in 0..<nums {
            var currArr = sentences[i].split(separator: " ").count

            if currArr > count {
                count = currArr
            }
        }

        return count
    }
}