class Solution {
    public int maximumWealth(int[][] accounts) {
        int result = 0;
        int n = accounts.length;
        int[] wealth = new int[n];

        for(int i = 0; i < accounts.length; i++){
            for(int j = 0; j < accounts[i].length; j++){
                wealth[i] += accounts[i][j];
            }
            result = Math.max(result, wealth[i]);
        }
        return result;
    }
}