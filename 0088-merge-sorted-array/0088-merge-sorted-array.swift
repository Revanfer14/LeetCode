class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int){
        var result: [Int] = []

        for i in 0..<m {
            result.append(nums1[i])
        }

        for i in 0..<n {
            result.append(nums2[i])
        }

        nums1 = result.sorted()
    }
}