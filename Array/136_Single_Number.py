# 時間複雜度 : O(n)
# 空間複雜度 : O(n)
class Solution:
    def singleNumber(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
S = Solution()
print(S.singleNumber([2,2,1]))

# 時間複雜度 : O(n)
# 空間複雜度 : O(n)
class Solution:
    def singleNumber(self, nums):
        data = {}
        for i in nums:
            data[i] = data.get(i,0)+1
        for i in data.keys():
            if data[i] == 1:
                return i
S = Solution()
print(S.singleNumber([4,1,2,1,2]))

# Bit Manipulation
# 時間複雜度: O(n)
# 空間複雜度: O(1)
# 概念:
# a^0 = a 且 a^a=0 且 a^b^a = a^a^b = 0^b = b 
class Solution:
    def singleNumber(self, nums):    
        a = 0
        for i in nums:
            a ^= i 
        return a 
S = Solution()
print(S.singleNumber([4,1,2,1,2]))
