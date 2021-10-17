# 時間複雜度 : O(n)
# 空間複雜度 : O(1)

class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
        result = len(wordsDict)
        p1 ,p2 = -1 , -1
        for i ,val in enumerate(wordsDict):
            if val == word1 :
                p1 = i
            elif val == word2 :
                p2 = i

            if p1 != -1 and p2 != -1 :
                result = min(result,abs(p1-p2))
        return result
S = Solution()
print(S.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"))