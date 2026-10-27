class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 99999
        max_profit = -99999
        for price in prices:

            if min_price > price:
                min_price = price

            profit = price - min_price
            # print(profit)
            if max_profit < profit:
                max_profit = profit

        return max_profit if max_profit > 0 else 0