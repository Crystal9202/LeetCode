class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()

        mn=min([ j-i  for i,j in zip(arr , arr[1:])])
        result=[[i,j] for i,j in zip(arr , arr[1:]) if j-i == mn ]
        return result
S = Solution()
print(S.minimumAbsDifference([4,2,1,3]))
