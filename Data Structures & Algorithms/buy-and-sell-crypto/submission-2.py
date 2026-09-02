class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = current price (sell) - minimum price seen so far (buy)
        i=0
        j=len(prices)

        max_profit=0
        min_buy=prices[i]
        for i in range(j):
            if prices[i]<min_buy:
                min_buy=prices[i]
            profit=prices[i]-min_buy
            
            if profit>max_profit:
                max_profit=profit
        return max_profit