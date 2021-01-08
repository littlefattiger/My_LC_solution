class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new ArrayList<Integer>();
        HashSet<Integer> s=new HashSet<Integer>();  
        for (int i: nums){
            s.add(i);
        }
        int n = nums.length;
        for(int i = 1; i <= n; i ++){
            if(!s.contains(i)){
                res.add(i);
            }
        }
        return res;
        
    }
}
