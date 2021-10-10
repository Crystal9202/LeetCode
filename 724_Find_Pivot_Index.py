class Solution:
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        
        for i ,val in enumerate(nums):
            if leftsum == S -val -leftsum :
                return i 
            
            else:
                leftsum += val 
        return -1
S = Solution()
print(S.pivotIndex([1,7,3,6,5,6]))