class Solution {
    public int[] getConcatenation(int[] nums) {
        int size = nums.length;
        int iter = size * 2;
        int[] result = new int[iter];
        int k = 0;

        for(int i = 0; i < iter; i++){
            if(k == size){
                k = 0;
            }
            result[i] = nums[k];
            k++;
        }

        return result;
    }
}