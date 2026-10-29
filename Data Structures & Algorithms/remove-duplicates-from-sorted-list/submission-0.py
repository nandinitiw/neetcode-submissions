# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        #declare head of new list and dummy variable to iterate through new_head
        new_head = ListNode(0)
        dummy = new_head
        #create hashset to keep track of node values we have seen
        seen = set()
        #iterate through head, at each iteration, check if head.val in seen

        while head:
            # -- if so, head = head.next
            # -- if not, add to hashset and new_head's next field points 
            # -- -- to this node.
            # -- if not, new_head = new_head.next
            if head.val not in seen:
                seen.add(head.val)
                dummy.next = head
                dummy = dummy.next
            head = head.next

            dummy.next = None
        
        return new_head.next

        