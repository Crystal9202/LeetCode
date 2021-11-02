# 時間複雜度: O(n + m), n = len(s) 且 m = len(t)
# 空間複雜度: O(n + m)
class Solution:
    def backspaceCompare(self, s, t) :
        def build(x):
            stack = []
            for i in x :
                if i != '#' :
                    stack.append(i)
                elif stack :
                    stack.pop()
                    
            return ''.join(stack)
        return build(s) == build(t)
S =Solution()
print(S.backspaceCompare(s = "ab#c", t = "ad#c"))
                