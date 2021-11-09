# 時間複雜度 :O(n)
# 空間複雜度 :O(1)
class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2,len(cost)):
            cost[i] = cost[i] + min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])
S =Solution()
print(S.minCostClimbingStairs([10,15,20]))