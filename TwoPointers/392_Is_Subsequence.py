#時間複雜度 :O(n)
#空間複雜度 :O(1)
class Solution:
    def isSubsequence(self, s, t):
        start = 0 

        for i ,val in enumerate(t):
            if start <= len(s)-1 and val == s[start] :   #注意兩個位置不能對調
                start += 1
        return start == len(s)
S = Solution()
print(S.isSubsequence(s = "abc", t = "ahbgdc"))
