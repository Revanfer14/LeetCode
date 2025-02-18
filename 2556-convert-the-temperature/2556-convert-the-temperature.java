class Solution {
    public double[] convertTemperature(double celsius) {
        double f;
        double k;
        double[] result = new double[2];

        f = (1.8 * celsius) + 32;
        k = celsius + 273.15;

        result[0] = k;
        result[1] = f;

        return result;
    }
}