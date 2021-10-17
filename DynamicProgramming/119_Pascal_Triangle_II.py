#時間複雜度 : O(**2)
class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for i in range(rowIndex):
            row = [i+j for i , j in zip([0]+row , row+[0])]
        return row
S = Solution()
print(S.getRow(3))
