class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_k = 1
        max_k = max(piles) #check if redundant
        min_ans = max_k

        while min_k < max_k:
            mid = (min_k+max_k)//2
            sum = 0

            for i in range(len(piles)):
                sum += (piles[i]+mid-1)//mid #rounds UP?
            
            if sum <= h:
                min_ans = min(min_ans, mid)
                max_k = mid
            
            else:
                min_k = mid+1

        return min_ans


