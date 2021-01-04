class Solution {
    public double averageWaitingTime(int[][] customers) {
        long start = 0;
        long finish = 0;
        long total = 0;
        for(int i = 0; i < customers.length; i ++){
            int a1 = customers[i][0];
            int a2 = customers[i][1];
            
            start = Math.max(finish, a1);
            
            finish = start + a2;
            total += finish - a1;
        }
        return (double) (total) /(double)(customers.length);
        
    }
}
