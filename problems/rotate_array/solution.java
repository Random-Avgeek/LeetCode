class Solution {
    public static void revarr(int[] arr,int start, int end){
        int temp;
        while(start<end){
            temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
    }
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        revarr(nums,0,nums.length-1);
        revarr(nums,0,k-1);
        revarr(nums,k,nums.length-1);
    }
        
}