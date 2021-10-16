class Solution:
    def arrayRankTransform(self, arr):
        data = {}
        arrSorted=sorted(arr)
        rank =1
            
        for i in arrSorted :
            if i not in data:
                data[i] = rank
                rank += 1
                
        for i , val  in enumerate(arr):
            arr[i] = data[val]
        
        return arr

S =Solution()
print(S.arrayRankTransform([40,10,20,30]))

        