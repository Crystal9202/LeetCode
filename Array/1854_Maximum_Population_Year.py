# 時間複雜度 : O(nlog(n))
# 空間複雜度 : O(n)
class Solution:
    def maximumPopulation(self, logs):
        data = []
        for birth , death in logs:
            data.append((birth , 1))
            data.append((death ,-1))
            
        data.sort()
        
        population = 0
        max_population = 0
        max_year = 0
        
        
        for i , j in data : 
            population += j
            if population > max_population :
                max_population = population 
                max_year = i
        return max_year
S = Solution()
print(S.maximumPopulation([[1993,1999],[2000,2010]]))
        