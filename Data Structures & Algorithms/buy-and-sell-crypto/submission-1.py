class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #need to buy low sell high, but linearly
        #o(n)
        #if max < 0 return 0
        #sliding window and two pointers - how do we do both at the same time?
        #
        #have one pointer for buy, one for sell buy<sell

        profit = 0
        minbuy = prices[0]

        for sell in prices:
            profit = max(profit, sell-minbuy) #maximum of curr profit and curr element - min buy
            minbuy = min(minbuy, sell)

        return profit