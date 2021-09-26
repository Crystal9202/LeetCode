#時間複雜度 : O(n)
class Solution:
    def maxProfit(self, prices):
        for i in range(1,len(prices)):
            prices[i-1] = prices[i]-prices[i-1]
        prices[len(prices)-1] = 0

        for i in range(1 ,len(prices)):
            if  prices[i-1] > 0 :
                prices[i] += prices[i-1]
        return max(prices)

S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))