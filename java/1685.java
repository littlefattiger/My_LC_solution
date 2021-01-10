class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int sum = 0;
        for (int num: nums){
            sum += num;
        }
        int n = nums.length;
        int[] res = new int[n];
        int pre_sum = 0;
        for (int i = 0; i < n; i ++){
            res [i] = sum - nums[i] *(n  - i) + nums[i] * i  -  pre_sum;
            pre_sum += nums[i];
            sum -= nums[i];
        }
        return res;
        
    }
}
