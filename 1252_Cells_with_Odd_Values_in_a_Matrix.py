# 時間複雜度 : O(m+n+L), L 是 indices 的長度
# 空間複雜度 : O(n+m)
class Solution:
    def oddCells(self, m, n, indices):
        rows = [0]*m
        cols = [0]*n

        for i , j in indices :
            rows[i] ^= 1
            cols[j] ^= 1
        
        R , C = sum(rows) ,sum(cols)
        return R*n + C*m - 2*R*C
S = Solution()
print(S.oddCells( m = 2, n = 3, indices = [[0,1],[1,1]]))
