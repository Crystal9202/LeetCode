class Solution:
    def rotateString(self, s, goal) :
        return len(s) == len(goal) and s in goal+goal 
            
S =Solution()
print(S.rotateString(s = "abcde", goal = "cdeab"))