# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        ans = ListNode(-1)
        tmp = ans

        while list1 and list2:

            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else: #list2.val >= list1.val
                tmp.next = list2
                list2 = list2.next
            
            tmp = tmp.next

            if not list1:
                tmp.next = list2
            else: #list2 is null
                tmp.next = list1


        return ans.next

        
            

            
