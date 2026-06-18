class Solution:
    def isValid(self, s: str) -> bool:
        #need to incorporate a stack of strings
        
        pairs = {"(":")", "{":"}", "[":"]"}

        str_stack = []

        for elem in s:
            if elem in ["(","{","["]:
                str_stack.append(elem)
                print(str_stack)
            
            else:
                if len(str_stack) == 0:
                    return False
                
                if pairs[str_stack.pop()] != elem:
                    return False
                
        return len(str_stack) == 0








"""
class Solution:
    def isValid(self, s: str) -> bool:
        #we know cannot close the parentheses
        #until the one started before is closed.
        #each one must have a pair


        if len(s)%2 != 0:
            return False

        mid = int(len(s)/2)

        s_chars1 = s[0:mid]
        s_chars2 = s[mid:len(s)]

        #closed invariant - must be closed w same type
        #ordering inv - must be closed in the correct order
        #once the opening is done, must ALL GET CLOSED.

        #two arrays, split down the middle
        #iterate through one forwards, 
        #iterate through the other backwards
        #make sure chars match at each iteration.

        for i in range(mid):
            if not self.isClosed(s_chars1[i],s_chars2[mid-1-i]):
                return False

        return True

    def isClosed(self, a: str, b: str) -> bool:
        if a=="(" and b==")":
            return True
        if a=="{" and b=="}":
            return True
        if a=="[" and b=="]":
            return True
        return False
"""

        