class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for char in s:
            if not char.isalnum():
                s = s.replace(char,"")

        print(s)
        i = 0

        while len(s)>0:
            j = len(s)-1
            if(s[i]!=s[j]):
                return False
            s = s[1:j]
        
        return True