# 時間複雜度 : O(n)
# 空間複雜度 : O(1)
class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total %3 != 0 : return False 

        count , cumsum ,target = 0 ,0 ,total//3
        for i in arr:
            cumsum += i
            if cumsum == target :
                count += 1
                cumsum =0 
        return count >= 3 

S = Solution()
print(S.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
