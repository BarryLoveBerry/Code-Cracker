#哈希表
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={} #创建哈希表
        for num in nums:#遍历数组
            if num in dic:#将出现的元素记录次数
                dic[num]+=1
            else:
                dic[num]=1
        big=0
        index=0
        for d in dic:#遍历字典
            if dic[d]>big:
                big=dic[d]
                index=d#找到出现次数最多的key
        return index
    
 # 排序
#思路如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为 【n/2】 的元素（下标从 0 开始）一定是众数。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

