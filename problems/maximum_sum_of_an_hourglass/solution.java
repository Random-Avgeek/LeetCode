class Solution {
    public int maxSum(int[][] arr) {
        int max = Integer.MIN_VALUE;
        int bestI, bestJ = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            for (int j = 0; j < arr[0].length - 2; j++) {
                int sum = 0;
                sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]
                        + arr[i + 2][j + 2];
                int oldmax = max;
                max = Math.max(max, sum);
                if (max > oldmax) {
                    bestI = i;
                    bestJ = j;
                }
            }
        }
        return max;
    }
}