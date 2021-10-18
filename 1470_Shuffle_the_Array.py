# 時間複雜度 : O(n)
# 空間複雜度 : O(n)
class Solution:
    def shuffle(self, nums, n):
        result = []
        for i,j in zip(nums[:n],nums[n:]) :
            result += [i,j]
        return result
S =Solution()
print(S.shuffle(nums = [2,5,1,3,4,7], n = 3))