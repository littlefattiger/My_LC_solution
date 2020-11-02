#https://leetcode.com/problems/array-of-doubled-pairs/
#from smallest to largest, and check whether the number can match, greedy idea

    def canReorderDoubled(self, A: List[int]) -> bool:
        c = Counter(A)
        A.sort()
        for v in A:
            if c[ v ]>0 and 2 * v in c and c[2 *v ] > 0:
                c[2 *v ] -= 1
                c[v] -= 1
        
        return all(i == 0 for i in c.values())
        
  #idea from lee215 is have some pruning
  
      def canReorderDoubled(self, A):
        c = collections.Counter(A)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True
