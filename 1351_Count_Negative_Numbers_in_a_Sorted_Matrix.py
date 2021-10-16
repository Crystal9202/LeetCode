class Solution:
    def countNegatives(self, grid):
        m , n  = len(grid) , len(grid[0])
        r ,  c , cnt = m-1 , 0 , 0 
        
        while r >=0 and c <= n-1 :
            if grid[r][c] < 0:
                cnt += n-c
                r -= 1
            else:
                c += 1 
        return cnt 
S = Solution()
print(S.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
