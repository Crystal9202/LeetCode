# 時間複雜度 : O(n)
# 空間複雜度 : O(1)
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i 
            count += 1 if i == candidate  else -1
        return candidate
S = Solution()
print(S.majorityElement([2,2,1,1,1,2,2]))


# 時間複雜度 : O(n)
# 空間複雜度 : O(n)
class Solution:
    def majorityElement(self, nums):
        data = {} 
        for i in nums :
            data[i] = data.get(i,0)+1
        for i in data.keys():
            if data[i] > len(nums)/ 2:
                return i
S = Solution()
print(S.majorityElement([2,2,1,1,1,2,2]))



