class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        start = 0
        seen = set()

        for i in range(len(s)):
            while(s[i] in seen):
                #maxlen = max(maxlen, len(seen))
                seen.remove(s[start])
                start+=1

            seen.add(s[i])
            maxlen = max(maxlen, i-start+1)
        
        #maxlen = max(maxlen, len(seen))
        return maxlen
