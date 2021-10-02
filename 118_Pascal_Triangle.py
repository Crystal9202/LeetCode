class Solution:
    def generate(self, numRows) :
        triangle = []
        for i in range(numRows):
            row = [0 for _ in range(i+1)]
            row[0],row[-1] = 1,1
        
            for j in range(1,len(row)-1):
                row[j] = triangle[i-1][j]+triangle[i-1][j-1]
            triangle.append(row)
        return triangle
S = Solution()
print(S.generate(5))