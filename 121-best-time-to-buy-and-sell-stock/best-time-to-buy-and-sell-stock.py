class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_index = 0
        sell_price = 0
        profits = [0]
        for index in range(1, len(prices)):
            if prices[index] < prices[buy_index]:
                buy_index = index
                sell_price = 0
            elif prices[index] >= sell_price:
                sell_price = prices[index]
                profit = sell_price - prices[buy_index]
                profits.append(profit)
        return max(profits)
            

            
        