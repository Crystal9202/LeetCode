class Solution:
    def minOperations(self, s) :
        even = 0
        for i ,val in enumerate(s):
            if int(val) != i%2 :
                even += 1
                
        return min(even , len(s)-even)
S = Solution()
print(S.minOperations("0100"))