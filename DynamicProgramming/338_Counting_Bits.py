# 時間複雜度: O(n)
# 空間複雜度: O(1)
# All whole numbers can be represented by 2N (even) and 2N + 1 (odd).
# For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when multiplying by ten in base 10).
# countBits(N) = countBits(2N)
# countBits(N) + 1 = countBits(2N + 1)

class Solution:
    def countBits(self, n):
        res = [0]*(n+1)
        
        for i in range(1 ,n+1):
            res[i] = res[i//2] + i%2
            
        return res
S =Solution()
print(S.countBits(2))