class Solution {
    public double myPow(double x, int n) {
        double result;
        long abs = Math.abs((long) n);

        if(n < 0){
            result =  1.00 / Math.pow(x, abs);
        } else{
            result =  Math.pow(x, abs);
        }

        return result;
    }
}