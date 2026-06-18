# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1rev = ""
        num2rev = ""

        while l1:
            num1rev += str(l1.val)
            l1 = l1.next
        while l2:
            num2rev += str(l2.val)
            l2 = l2.next
        
        num1 = ""
        for i in range(len(num1rev)-1,-1,-1):
            num1+=num1rev[i]
        num2 = ""
        for i in range(len(num2rev)-1,-1,-1):
            num2+=num2rev[i]

        sum = int(num1)+int(num2)
        sumstring = str(sum)

        dummy = ListNode()
        curr = dummy

        for i in range(len(sumstring) - 1, -1, -1):
            curr.next = ListNode(int(sumstring[i]))
            curr = curr.next

        ans = dummy.next
        return ans

        



        