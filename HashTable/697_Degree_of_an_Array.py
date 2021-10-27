時間複雜度 : O(n)
空間複雜度 : O(n)
class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        degree = 0 
        result = 0
        
        for i , val in enumerate(nums):
            count[val] = count.get(val,0) +1 
            first.setdefault(val,i)
            
            if count[val] > degree :
                degree = count[val]
                result = i - first[val] +1 
                
            if  count[val] == degree :
                result = min(result , i-first[val] +1)
        
        return  result
S = Solution()
print(S.findShortestSubArray([1,2,2,3,1]))


