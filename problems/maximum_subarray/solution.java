class Solution {
    public int maxSubArray(int[] nums) {
        int maximum = nums[0];
        int maximized = nums[0];
        for (int i = 1; i < nums.length; i++) {
            maximized = Math.max(nums[i], maximized + nums[i]);
            if (maximized > maximum) {
                maximum = maximized;
            }
        }
        
        return maximum;
    }
}