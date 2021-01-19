// people -> state -> substate

class Solution {
    public int minimumTimeRequired(int[] jobs, int k) {
        int[][] dp = new int[13][4096];
        for(int i = 0; i < 13; i ++ ){
            for(int j = 0; j < 4096; j ++){
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        
        dp[0][0] = 0;
        int n = jobs.length;
        int[] subset_time = new int[4096];
        for (int subset = 0; subset < (1<<n); subset++){
            int tot = 0;
            for (int i = 0; i < n; i ++){
                if(  ((1 << i) & subset) > 0 ){
                    tot += jobs[i];
                }
            }
            subset_time[subset] = tot;
                
            
        }
        
        for (int i = 1; i < k + 1; i ++){
            for (int state = 0; state < ( 1<<n); state ++){
                
                for(int subset = state; subset > 0; subset = (subset-1)&state){
                    dp[i][state] = Math.min(dp[i][state],Math.max(dp[i - 1][state - subset],subset_time[subset] ) );
                    
                }
                
            }
        }
        
        return dp[k][(1<<n) - 1];
        
    }
}
