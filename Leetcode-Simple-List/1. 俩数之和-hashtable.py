class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 创建哈希表
        hashtable = dict()
        for i in range (len(nums)):
            if target - nums[i] in hashtable: #如果哈希表中存在
                return [hashtable[target - nums[i]], i] #返回差值索引和当前的i
            hashtable[nums[i]] = i #将list中的值 对应上 它的索引

        return []# 如果答案返回 []
