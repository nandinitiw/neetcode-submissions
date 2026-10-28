# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #null check for list1, list2
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        #declare head of new list
        dummy = ListNode(0)
        #create var to return at the end
        head = dummy
        #at each step, compare the current node from list1 and list2
        while list1 and list2:
            #if list1.val <= list2.val, then dummy.next = list1 and vice versa
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        #repeat until !list1.next or !list2.next
        #if !list1, head.next = remaining nodes in list2, and vice versa
        if not list1:
            dummy.next = list2
        elif not list2:
            dummy.next = list1
        dummy = dummy.next

        #return head of new list
        return head.next
        
            

            
