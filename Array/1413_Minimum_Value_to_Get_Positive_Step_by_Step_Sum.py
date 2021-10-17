# 時間複雜度 : O(n)
# 空間複雜度 : O(1)
class Solution:
    def minStartValue(self, nums) :
        prefix_sum = 0
        minStart = 1

        for num in nums:
            prefix_sum += num
            minStart = max(minStart , 1-prefix_sum)
        return minStart 
S = Solution()
print(S.minStartValue([-3,2,-3,4,2]))