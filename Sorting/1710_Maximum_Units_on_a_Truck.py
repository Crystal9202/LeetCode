# 時間複雜度: O(n)
# 空間複雜度 :O(1)
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1] , reverse= True)
        result = 0

        for i , j in boxTypes:
            if i >= truckSize :
                result += j*truckSize
                return result
            else:
                result += i*j 
                truckSize -= i 
S = Solution()
print(S.maximumUnits( [[1,3],[2,2],[3,1]], truckSize = 4))