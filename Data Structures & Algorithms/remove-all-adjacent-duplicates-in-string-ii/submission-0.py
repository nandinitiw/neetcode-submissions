class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #stack of characters in s
        #we keep the count of consecutive characters in the stack
        #as we remove letters, we decrement i and len of string var

        n = len(s)
        i=0
        stack = []

        while i<n:
            #on the first iteration OR when 2 dif characters in a sequence
            #listing i==0 before skips if before arr out of bounds
            if i==0 or s[i]!=s[i-1]:
                stack.append(1)
            else:
                #increment counter
                stack[-1]+=1
                if stack[-1]==k:
                    stack.pop()
                    s = s[0:i-k+1]+s[i+1:len(s)]
                    #del s[i-k+1:i+1]
                    i-=k
                    n-=k
            
            i+=1
        
        return s


        