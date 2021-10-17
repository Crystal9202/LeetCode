# 時間複雜度 : O(n)
# 空間複雜度 : O(1)
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        mx=max(candies)
        for i ,val in enumerate(candies):
            if val + extraCandies >= mx :
                candies[i] = True
            else:
                candies[i] = False
        return candies
S = Solution()
print(S.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))