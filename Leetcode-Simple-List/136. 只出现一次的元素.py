#位运算
#线性时间复杂度和常数空间复杂度
#异或运算符
#1. 任何数和0做异或运算，结果仍然是原来的数，a⊕0=a。
#2. 任何数和其自身做异或运算，结果是0，a⊕a=0。
#3. 异或运算满足交换律和结合律， a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        all_val = 0
        for i in nums:
            all_val^=i

        return all_val
