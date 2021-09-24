#一個迴圈: 時間複雜度o(n)
class Solution:
    def removeDuplicates(self, nums):
        start = 0
        for i in range(len(nums)):
            if nums[i] != nums[start]:
                nums[start +1] = nums[i]
                start += 1
        return start +1
P=Solution()
print(P.removeDuplicates([1,1,2]))
