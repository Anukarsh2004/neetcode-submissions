class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        buy = prices[0]
        currMax = prices[0]

        for price in prices[1:]:
            if price < buy:
                profit = currMax - buy
                res += profit
                buy = price
                currMax = price
            elif price < currMax:
                profit = currMax - buy
                res += profit
                buy = price
                currMax = price
            else:
                currMax = price
        
        res += currMax - buy
        
        return res

        