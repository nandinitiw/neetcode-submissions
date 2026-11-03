class Solution:
    def hammingWeight(self, n: int) -> int:
        #bit manipulation - right shifts?

        #loop bit by bit by shifting right [0, 31]
        #take shifted number & 1 (1 if lowest bit = 1, 0 o/w)

        count = 0
        for i in range(31):
            count += n&1 #1 if set, 0 if not
            n=n>>1
        
        return count

        