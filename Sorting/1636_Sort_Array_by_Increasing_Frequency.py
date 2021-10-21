# 時間複雜度 : O(nlog(n))
# 空間複雜度 : O(n)
class Solution:
    def frequencySort(self, nums):
        count = {}
        for i in nums :
            count[i] = count.get(i,0)+1
        nums.sort(key=lambda x : (count[x], -x ))  
        return nums
S = Solution()
print(S.frequencySort([1,1,2,2,2,3]))