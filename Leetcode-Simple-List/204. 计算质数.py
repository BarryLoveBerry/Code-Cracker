# 纯暴力
class Solution:
    def countPrimes(self, n: int) -> int:
        def is_primes(c):
            for i in range(2, int(sqrt(c))+1):
                if c % i == 0:
                    return False
            return True
        ans = 0
        for j in range(2, n+1):
            if is_primes(j):
                ans += 1
        return ans

#埃氏筛选
#西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，
#减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，这方法被称作厄拉多塞筛法(Sieve of Eeatosthese)。
#
#具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
#现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于n的各数都画了圈或划去为止。
#这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。


class Solution:
    def countPrimes(self, n: int) -> int:
        # 定义数组标记是否是质数
        is_prime = [1] * n
        
        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                for j in range(i*i, n, i):
                    is_prime[j] = 0

        return count

