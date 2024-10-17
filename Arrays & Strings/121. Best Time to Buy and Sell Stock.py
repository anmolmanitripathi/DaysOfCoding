#URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) <= 1):
            return 0

        buyIndex = 0
        maxProfit = 0

        for i in range(1, len(prices)):
            if (prices [i] - prices[buyIndex]) < 0:
                buyIndex = i
            elif (prices [i] - prices[buyIndex]) > maxProfit:
                maxProfit = prices [i] - prices [buyIndex]

            if prices[buyIndex] > prices [i]:
                buyIndex = i

        return maxProfit
        
        # buyIndex = 0
        # for i in range(1, len(prices)):
        #     if prices[buyIndex] > prices[i]:
        #         buyIndex = i

        # if buyIndex == (len(prices) - 1):
        #     return 0
        
        # sellIndex = buyIndex + 1
        # for i in range(sellIndex, len(prices)):
        #     if prices[sellIndex] < prices[i]:
        #         sellIndex = i

        # return prices[sellIndex] - prices[buyIndex]

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)