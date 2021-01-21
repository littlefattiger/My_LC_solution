class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=[i for i in s.lower() if i.isalnum()]
        return r==r[::-1]
