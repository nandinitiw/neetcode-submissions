class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #declare a variable to hold longest substring found so far
        longest = 0
        #hashmap to hold characters seen already
        seen = set()
        #declare left and right pointers to first character of string
        left = 0
        #iterate through string by moving right pointer
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            #if right pointer in seen, move left pointer up until window is valid
            seen.add(s[right])
            longest = max(longest, right-left+1)
        #at each iteration, set longest substring to max of prev value
        # -- and current window

        return longest

