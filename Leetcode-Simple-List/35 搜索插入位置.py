#二分查找
#排序数组中寻找是否存在一个目标值 - 二分法O（logn）
# nums[pos−1]<target≤nums[pos]
#循环条件 左索引小于等于右索引

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left =  mid + 1
        return left



#下面答案时间复杂度O（n）
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            elif nums[i] < target and i == len(nums)-1:
                return i+1
                
"""                
