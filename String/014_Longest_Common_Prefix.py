# 時間複雜度 :O(m*n)，m 是 strs 裡面最小字串的長度，n 是strs 的長度
# 空間複雜度 :O(m)，m 是 strs 裡面最小字串的長度
# 注意 len(String) 與 len(List) 的時間複雜度都是 O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs :
            return ""

        shortest = min(strs , key =len)

        for i ,j in enumerate(shortest):
            for other in strs:
                if other[i] != j :
                    return shortest[:i]
        return shortest
S = Solution()
print(S.longestCommonPrefix(["flower","flow","flight"]))
