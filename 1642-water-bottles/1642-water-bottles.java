class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int x = 0;
        int y = 0;
        int result = numBottles;

                while(numBottles >= numExchange) {
                    x = numBottles / numExchange;
                    y = numBottles % numExchange;

                    result += x;

                    numBottles = x + y;
            }
            
        return result;
    }
}