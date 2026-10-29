# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #declare head of new linked list
        #dummy head to traverse linked list
        #while list1 and list2 are both non-null, traverse them
        #at each iteration, if list1.val<=list2.val, dummy points to list1
        #then, list1 = list1.next and dummy=dummy.next 
        #once either list1 or list2 are null, dummy should point to remaining list
        #return pointer to first element in new linked list

        head = ListNode(0)
        dummy = head

        while list1 and list2:
            if list1.val<=list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if not list1:
            dummy.next = list2
        if not list2:
            dummy.next = list1

        return head.next 
        
            

            
