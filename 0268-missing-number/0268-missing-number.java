class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = n* (n+1)/2;
        int ts =0;
        for(int i : nums){
             ts += i ;
        }
        int mn = sum - ts;
        return mn;    
    }
}