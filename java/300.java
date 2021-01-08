class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> dp = new ArrayList<Integer>();
        int n = nums.length;
        for(int i = 0; i < n; i ++){
            int index = bisect_left(dp, nums[i]);
            if (index >= dp.size()){
                dp.add(Integer.MAX_VALUE);
            }
            
            dp.set(index, nums[i] < dp.get(index) ? nums[i]:dp.get(index) );
            
        }
        return dp.size();
    }
    
    
    public int bisect_left(List<Integer> nums, int v){
        int n = nums.size();
        int l = 0;
        int r = n;
        while(l < r){
            int m = (l + r) /2;
            if(nums.get(m) >= v){
                r = m;
            }else{
                l = m + 1;
            }
        }
        return l;
    }
}
