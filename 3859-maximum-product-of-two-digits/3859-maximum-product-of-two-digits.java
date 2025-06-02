class Solution {
    public int maxProduct(int n) {
        int len = String.valueOf(n).length();

        int[] max = new int[len];
        int result = 0;

        String str = Integer.toString(n);

        int digit = 0;

        for(int i = 0; i < len; i++){
            digit = Character.getNumericValue(str.charAt(i));
            max[i] = digit;
        }

        Arrays.sort(max);

        result = max[max.length - 1] * max[max.length - 2];

        return result;
    }
}