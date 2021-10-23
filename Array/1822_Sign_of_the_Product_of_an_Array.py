# 時間複雜度 : O(n)
# 空間複雜度 : O(1)
class Solution:
    def arraySign(self, nums):
        result = 1
        for i in nums :
            result *= i 
        if result > 0 :  return 1
        elif result < 0 :  return -1 
        else:  return 0 
S =Solution()
print(S.arraySign([-1,-2,-3,-4,3,2,1]))