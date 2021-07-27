# 暴力解法

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curval = nums[0]    #当前和为数组第一个，用来表示前i项sum
        maxval = curval   # 当前最大值等于数组当前值 ，用来保存最大连续子序列的sum
        length = len(nums)
        for i in range(1,length):
            if curval+nums[i] > nums[i]:   #前i项和 如果大于第i项的元素，说明最大子序列可能还在i的右侧
                maxval = max(maxval, curval+nums[i])    #更新最大值
                curval = curval+nums[i]       #更新前i项和
            else:   #反之，最大子序列可能出现在i的左侧，停止遍历
                maxval = max(maxval,curval,nums[i],curval+nums[i])
                curval = nums[i]
        return maxval
      
#DP,关键是找出状态转移方程

#方程为f(i)=max{f(i−1)+nums[i],nums[i]}（）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        curval = nums[0]
        length = len(nums)
        for i in range(length):
            pre = max(pre + nums[i], nums[i])
            curval = max(curval,pre)
        
        return curval
                    
