# 時間複雜度 : O(n)
# 空間複雜度 : O(n)
class Solution:
    def containsDuplicate(self, nums):
        data = {}
        for i in nums :
            data[i] = data.get(i,0)+1 
        for key,val  in data.items():
            if val >=2 :
                return True
            else:
                False
S = Solution()
print(S.containsDuplicate([1,2,3,4]))

# 時間複雜度 : 使用內建函式不討論
class Solution:
    def containsDuplicate(self, nums):
        return len(nums)  != len(set(nums))
S = Solution()
print(S.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))