# stack 堆疊
# 時間複雜度 : O( n + n +m ) => O(n) 注意在這裡 nums1 是 nums2的子集，所以 m <= n
# 空間複雜度 : O(n)
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        data ={}
        stack =[]
        result = []
        for i in nums2:
            while stack and stack[-1] < i :
                data[stack.pop()] = i
            stack.append(i)

        for i in nums1:
            result.append(data.get(i,-1))

        return result

S = Solution()
print(S.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))



# Brute Force 暴力法
# 時間複雜度 : O(n*m), m = len(nums1) 且 n = len(nums2)
# 空間複雜度 : O(n) ,注意 result 是我們必要得返回結果，所以我們這裡可以不用算進去空間複雜度
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        data = {}
        result = []
        for i,val in enumerate(nums2):
            data[val] = i

        for i,val in enumerate(nums1):
            for j in range(data[val]+1 , len(nums2)):
                if nums2[j] > val :
                    result.append(nums2[j])
                    break 
            else:
                result.append(-1)

        return result
S = Solution()
print(S.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])) 