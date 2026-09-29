class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total=0
        for i in t:
            total+=ord(i)
        for i in s:
            total-=ord(i)
        return chr(total)