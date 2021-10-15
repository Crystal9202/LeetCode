# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def sumZero(self, n):
        a = list(range(1,n))
        return a + [-n*(n-1)/2]
