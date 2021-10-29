class Solution:
    def firstUniqChar(self, s) :
        mapping ={}
        for i in s:
            mapping[i] = mapping.get(i,0)+1
        for i ,val in enumerate(s):
            if mapping[val] == 1:
                return i
        return -1
S = Solution()
print(S.firstUniqChar("leetcode"))
