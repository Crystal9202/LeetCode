# 時間複雜度 :O(n)
# 空間複雜度 :O(1)
class Solution:
    def fib(self, n: int) -> int:
        a ,b = 0, 1

        for i in range(0,n):
            a, b = b , a+b
        return a
S = Solution()
print(S.fib(3))