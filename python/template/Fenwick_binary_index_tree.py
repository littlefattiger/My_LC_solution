# the query, is to search position from 0 to i - 1, not include i
class FenwickTree():
    
    def __init__(self, n):
        self.pre_sum = [0] * (1 + n)
        
    def update(self, i, delta):
        while i < len(self.pre_sum):
            self.pre_sum[i] += delta
            i += i & (-i)
    
    def query(self,i):
        s = 0
        while i >0:
            s += self.pre_sum[i]
            i -= i & (-i)
        
        return s
