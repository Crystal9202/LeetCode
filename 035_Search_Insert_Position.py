# 時間複雜度: O(n)
# class Solution:
#     def searchInsert(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i] >= target :
#                 return i
#         return len(nums) 
# S = Solution()
# print(S.searchInsert([1,3,5,6],5))





# Classical binary search  
# 時間複雜度 O(log(n)):
class Solution:
    def searchInsert(self, nums, target):
        beg, end = 0, len(nums) 
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg
S = Solution()
print(S.searchInsert([1,3,5,6],5))