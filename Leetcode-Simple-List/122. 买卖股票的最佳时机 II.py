#暴力和贪心
#需要说明的是，贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程。
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(1,len(prices)):
        #     if prices[i]>prices[i-1]:
        #         profit +=(prices[i]-prices[i-1])
        # return profit
        ans = 0
        for i in range(1,len(prices)):
            ans += max(0,prices[i]-prices[i-1])
        return ans
