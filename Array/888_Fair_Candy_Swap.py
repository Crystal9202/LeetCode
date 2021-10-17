# 時間複雜度 : O(n + m) , n =len(aliceSizes) 且 m = len(bobSizes)
# 空間複雜度 : O(m)
# 注意注意! x in list 時間複雜度 O(n) ; x in set 時間複雜度 O(1) ; x in dict 時間複雜度 O(1)

class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
       diff = sum(bobSizes) - sum(aliceSizes)
       diffB = set(bobSizes)
       
       for i ,val in enumerate(aliceSizes):
           if val +diff/2 in diffB:
               return [val , val+diff/2]
S = Solution()
print(S.fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))



