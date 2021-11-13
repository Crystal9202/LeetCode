# 時間複雜度: O(m*n)
# 空間複雜度: O(1)
class Solution:
    def islandPerimeter(self, grid) -> int:
        r , c = len(grid) ,len(grid[0])
        result = 0
        
        for row in range(0,r):
            for col in range(0,c):
                if grid[row][col] == 1:
                    result += 4
                    
                    if row -1 >= 0 and grid[row-1][col] == 1 :
                        result -= 2
                    
                    if col -1 >=0 and grid[row][col-1] == 1 :
                        result -= 2
        return result
S =Solution()
print(S.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))