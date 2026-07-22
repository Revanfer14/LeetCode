class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let arr = Array(s)

        var seen = Set<Character>()

        var left = 0
        var maxLen = 0

        for right in 0..<arr.count {
            while (seen.contains(arr[right])) {
                seen.remove(arr[left])
                left += 1
            }

            seen.insert(arr[right])
            maxLen = max(maxLen, right-left+1)
        }

        return maxLen
    }
}