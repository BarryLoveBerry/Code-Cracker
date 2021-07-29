#暴露法 超出时间限制

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxval = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                curval = prices[i] - prices[j]
                if curval <= maxval:
                    maxval = curval
                else:
                    continue
        return abs(maxval)
      
 # 一次遍历 DP思想
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = max(prices) # 记录最小的谷值
        max_profit = 0 # 记录最大利润

        for i in prices:
            if i<min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit
