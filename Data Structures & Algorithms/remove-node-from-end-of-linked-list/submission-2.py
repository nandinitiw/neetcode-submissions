# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        dummylen = head
        len = 0

        while dummylen:
            dummylen = dummylen.next
            len += 1
        
        if n==len:
            return head.next

        for i in range(len-n-1):
            dummy = dummy.next
        
        if dummy.next:
            dummy.next = dummy.next.next

        return head
        