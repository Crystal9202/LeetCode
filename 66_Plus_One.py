# 時間複雜度: O(n)
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1 
            if digits[i] != 10 :
                return digits
            digits[i] =  0
        return [1] + digits

S = Solution()
print(S.plusOne([4,3,2,1]))
        