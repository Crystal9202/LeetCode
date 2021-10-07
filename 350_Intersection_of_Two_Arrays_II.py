# 時間複雜度: O(n + m), n = len(nums1) 且 m = len(nums2)
# 空間複雜度 : O(min(m,n))
class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        data = []

        for i in nums1 :
            count[i] = count.get(i,0)+1

        for i in nums2:
            if i in count and count[i] >0 :
                data.append(i)
                count[i] -= 1
                
        return data
S = Solution()
print(S.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
