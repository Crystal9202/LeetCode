# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-" ,'').replace(" ","")
        res = []
        
        for i in range(0,len(number),3) :
            if len(number) -i != 4 :
                res.append(number[i:i+3])
            else:
                res.extend([number[i:i+2],number[i+2:]])
                break
                
        return "-".join(res)
S = Solution()
print(S.reformatNumber("1-23-45 6")) 