# https://leetcode.com/problems/add-two-numbers/
# very straightforward
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        
        r = ListNode(0)
        head = r
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            tot = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            r.next = ListNode(tot)
            l1 = l1.next
            l2 = l2.next
            r = r.next
            
        while l1:
            tot = (l1.val  + carry) % 10
            carry = (l1.val + carry) // 10
            r.next = ListNode(tot)
            l1 = l1.next
            r = r.next
            
 
        while l2:
            tot = (l2.val  + carry) % 10
            carry = (l2.val + carry) // 10
            r.next = ListNode(tot)
            l2 = l2.next
            r = r.next
        
        if carry:
            r.next = ListNode(carry)
            
        return head.next
