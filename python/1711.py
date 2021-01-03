class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        c = Counter(deliciousness)
        is_two_power = [2 ** i for i in range(0, 22)]
        # print(is_two_power)
        # print(c)
        res = 0
        for number in is_two_power:
            for v in c:
                
                if number - v in c:
                    # print(number,number - v, v)
                    # print(c[v])
                    # print(c[number - v])
                    if number - v == v:
                        res += (c[v] * (c[v] - 1)) /2
                        # print(res,v, number-v, c[v], c[number - v] )
                    else:
                        res += c[v] * c[number - v]/2
                        # print(res,v, number-v, c[v], c[number - v] )
        return int(res) %(10** 9 + 7)
