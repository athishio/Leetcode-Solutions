class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i,c in enumerate(s,start=1):
            reverse_pos=26-(ord(c)-ord('a'))
            ans+=reverse_pos*i
        return ans