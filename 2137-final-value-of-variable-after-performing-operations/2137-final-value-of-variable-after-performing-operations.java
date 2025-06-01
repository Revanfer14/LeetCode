class Solution {
    public int finalValueAfterOperations(String[] operations) {
        String x = "++X";
        String x1 = "X++";
        
        int result = 0;

        for(int i = 0; i < operations.length; i++){
            if(operations[i].equals(x) || operations[i].equals(x1)){
                result += 1;
            } else {
                result -= 1;
            }
        }

        return result;
    }
}