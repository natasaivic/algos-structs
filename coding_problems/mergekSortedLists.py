# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, 
# each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if lists is None: 
            return 
        result = []
        for i in lists:
            current = i
            while current is not None:
                result.append(current.val)
                current = current.next
        
        if result is None: 
            return
        result.sort()
        head = ListNode()
        m=head
        for k in result:
            m.next = ListNode(k)
            m = m.next
        return head.next
