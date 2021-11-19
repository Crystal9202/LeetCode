# 時間複雜度:O(n)
# 空間複雜度:O(n)
class Solution:
    def rotate(self, nums, k) :
        k=k%len(nums)

        nums[:]=nums[len(nums)-k:] + nums[:len(nums)-k]