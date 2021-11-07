# 時間複雜度: O(n)
# 空間複雜度: O(1)
# Fibonacci Number
class Solution:
    def climbStairs(self, n) :
        a , b = 1 , 1

        for _ in range(n):
            a ,b = b , a +b 
        return a 
S = Solution()
print(S.climbStairs(2))