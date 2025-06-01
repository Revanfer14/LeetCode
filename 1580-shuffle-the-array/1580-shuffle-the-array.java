class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] x = new int[n];
        int[] y = new int[n];

        int k = 0;
        int p = 0;

        for(int i = 0; i < nums.length; i++){
            if(i >= n){
                y[k] = nums[i];
                k++;
            } else {
                x[p] = nums[i];
                p++;
            }
        }

        k = 0;
        p = 0;

        int[] result = new int[nums.length];

        for(int j = 0; j < nums.length; j++){
            if(j % 2 == 0){
                result[j] = x[p];
                p++;
            } else {
                result[j] = y[k];
                k++;
            }
        }

        return result;
    }
}