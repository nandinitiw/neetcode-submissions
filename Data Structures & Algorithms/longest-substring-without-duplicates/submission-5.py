class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use 2 pointers, both at the first character of s
        #declare a hashset to keep track of characters we have already seen
        #declare var to keep track of longest substring so far

        #keep left pointer in place, move right pointer until w find a character
        #-- already in the hashset

        #if we find a repeating character, shrink from the left until that element
        # -- is no longer in the window
        seen = set()
        longest = 0

        left = 0 
        right = 0

        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])                
            longest = max(longest, right-left+1)
            right +=1

        return longest



