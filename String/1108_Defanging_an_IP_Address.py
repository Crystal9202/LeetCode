# 時間複雜度 :O(n)
# 空間複雜度 :O(n)
# str.replace() 時間複雜度 O(n)
class Solution:
    def defangIPaddr(self, address):
        return address.replace("." ,"[.]")
S =Solution()
S.defangIPaddr("1.1.1.1")

# 時間複雜度 :O(n)
# 空間複雜度 :O(n)
# str.join() 時間複雜度 O(n)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split("."))
S =Solution()
S.defangIPaddr("1.1.1.1")