class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a,b) ->  (b[1] - a[1]) );
        int n = boxTypes.length;
        int res = 0;
        for (int i = 0; i < n; i ++){
            int box  = boxTypes[i][0];
            int unit = boxTypes[i][1];
            if (box <= truckSize){
                res += box * unit;
                truckSize -= box;
            }else{
                res += truckSize * unit;
                break;
            }
        }
        return res;
        
    }
}
