class Solution {
    public int divide(int dividend, int divisor) {
        int result;

        if(dividend < 0 && divisor < 0){
            result = (int) Math.abs(Math.floor(dividend /divisor));
        } else{
            result = (int) Math.floor(dividend / divisor);
        }
        return result;
    }
}