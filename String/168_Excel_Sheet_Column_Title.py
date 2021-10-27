# 時間複雜度: O(log(n)), n = columnNumber
# 空間複雜度: O(1), 不算 resultclass Solution:
class Solution:
    def convertToTitle(self, columnNumber) :
        capital = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        result = ''

        while columnNumber :
            result = capital[(columnNumber - 1) %26 ] +result
            columnNumber = (columnNumber -1) // 26 
        return result
S = Solution()
print(S.convertToTitle(29))
