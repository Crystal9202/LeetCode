# 時間複雜度 : O(n)
# 空間複雜度 : O(n)
# 注意 : set() 的時間複雜度 O(n)，空間複雜度 O(n)

class Solution:
    def findDisappearedNumbers(self, nums ):
        lgh = len(nums)
        nums = set(nums)
        
        return [i  for i in range(1,lgh +1) if i not in nums ]
S = Solution()
print(S.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
