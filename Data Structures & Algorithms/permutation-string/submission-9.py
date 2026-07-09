class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        target = {}

        if len(s1)>len(s2):
            return False

        # Build frequency counts
        for i in range(len(s1)):      
            target[s1[i]] = target.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        # Build first window counts

        if window == target:
            return True

        left = 0

        for right in range(len(s1), len(s2)): 
            # Add s2[right]
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Remove s2[left]
            window[s2[left]] = window.get(s2[left],0) - 1
            if window[s2[left]] == 0:
                 del window[s2[left]]

            left += 1

            if window == target:
                return True

        return False
