# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, 
# and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cr,sm = 0,0
        r = ans = ListNode()
        while l1 or l2 or cr:
            d1, d2 = 0, 0
            if l1:
                d1 = l1.val
            if l2:
                d2 = l2.val
            sm = d1 + d2 + cr
            cr = sm//10
            r.next = ListNode(sm%10)
            r = r.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)

            # update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None