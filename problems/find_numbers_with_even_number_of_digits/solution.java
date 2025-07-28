class Solution {
    public int findNumbers(int[] nums) {
        int counteven = 0;

        if (nums.length == 0) {
            return 0;
        }

        for (int num : nums) {

            if (String.valueOf(num).length() % 2 == 0) {
                counteven += 1;
            }
        }
        return counteven;
    }
}