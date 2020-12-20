# you only need to deal with a special case for 4 items left

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        res = []
        n = len(number)
        for i in range(0, n, 3 ):
            if n - i != 4:
                res.append(number[i:i + 3])
            else:
                res.append(number[i:i + 2])
                res.append(number[i + 2:n])
                break
                
        return '-'.join(res)
