class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = [] #store indices for which we need to find next lesser price
        #iterate through prices, comparing value to the next one
        for idx in range(len(prices)):
            #pop idx that needs to find next lesser price
            while stack and prices[idx]<=prices[stack[-1]]:
                prices[stack[-1]] -= prices[idx]
                stack.pop()
            stack.append(idx)
            
        return prices

