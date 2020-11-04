# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# refer answer from lee215. Here we use a list with " is to simulate the situation, need to familar with it, add a new " at the beginning to get result, every ( has a " to store its current value
# sendond solution is amazing

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
        
    def reverseParentheses(self, s: str) -> str:
        opened = []
        pair = {}
        for i, v in enumerate(s):
            if v == '(':
                opened.append(i)
            elif v == ')':
                j = opened.pop()
                pair[i] = j
                pair[j] = i
        i = 0
        d = 1
        res = []
        while i < len(s):
            if s[i] in '()':
                d = -d
                i = pair[i]
            else:
                res.append(s[i])
            
            i += d
        return ''.join(res)
        
