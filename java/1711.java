class Solution {
    public int countPairs(int[] deliciousness) {
        Map<Integer, Integer> myMap = new HashMap<Integer, Integer>();
        int n = deliciousness.length;
        long res = 0;
        
        for(int v: deliciousness){
            for(int i = 0; i < 22; i ++){
                int v2 = (int)Math.pow(2, i) - v;
                if(myMap.containsKey(v2)){
                    res += myMap.get(v2);
                    res %=  1000000007;
                }
            }
            myMap.put(v, myMap.getOrDefault(v, 0) + 1);
            
        }
        
        return (int)res % 1000000007;
        
    }
}
