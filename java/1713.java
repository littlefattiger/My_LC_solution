// here I use a binary search for the array list container
class Solution {
    public int minOperations(int[] target, int[] arr) {
        Map<Integer, Integer> dp = new HashMap<Integer, Integer>();
        int n = target.length;
        int m = arr.length;
        for(int i= 0; i < n; i++){
            dp.put(target[i],i);
        }
        List<Integer> dp2 = new ArrayList<Integer>();
        for(int a: arr){
            if (!dp.containsKey(a)){
                continue;
            }
            int index = Collections.binarySearch(dp2, dp.get(a));
            if(index <= -1){
                index = -(index + 1);
            }
            
            if (  index >= dp2.size()   ){
                dp2.add(0);
            }
            
            dp2.set(index, dp.get(a));
        }
        return n - dp2.size();
        
        
        
    }
}
