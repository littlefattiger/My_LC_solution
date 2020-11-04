https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# refer answer from lee215. Here we use a list with " is to simulate the situation, need to familar with it


class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ['']
        
        for v in s:
            if v =='(':
                res.append('')
            elif v ==')':
                temp = res.pop()
                res[-1] += temp[::-1]
            else:
                res[-1] += v
        
        return ''.join(res)
        
