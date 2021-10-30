# 時間複雜度 :O(n)
# 空間複雜度 :O(1) ，result 不計入

class Solution:
    def fizzBuzz(self, n):
        result = []
        for i in range(1,n+1):
            if i%3 ==0 and i%5 ==0 :
                result.append('FizzBuzz')
            elif i%3 ==0 :
                result.append('Fizz')
            elif i%5 ==0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
S = Solution()
print(S.fizzBuzz(n = 3))