# 時間複雜度: O(n + m), n = len(nums1) 且 m = len(nums2)
# 空間複雜度: O(n + m)
# 注意像 set1 = set(nums1) 這種把列表轉集合的操作時間複雜度是: O(n)
class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
S = Solution()
print(S.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))       



# 時間複雜度 : O(n*m) , n = len(nums1) 且 m = len(nums2)
# 空間複雜度 : O(min(n,m))
class Solution:
    def intersection(self, nums1, nums2):
        data = []
        for i in nums1:
            if i in nums2  and i not in data:
                data.append(i)
        return data
S = Solution()
print(S.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
