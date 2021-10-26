# 時間複雜度 :O(max(n,m)) ,n =len(a) and m=len(b)
# 空間複雜度 :O(max(n,m))
class Solution:
    def addBinary(self, a, b) :
        result = ''
        carry = 0

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a :
                carry += int(a)
            if b:
                carry += int(b)

            result += str(carry%2)
            carry //= 2
        return result[::-1]
S =Solution()
print(S.addBinary(a = "11", b = "1"))