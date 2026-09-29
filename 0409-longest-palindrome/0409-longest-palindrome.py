class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        ans=0
        for i in count.values():
            ans+=(i//2)*2
        if ans<len(s):
            ans+=1
        return ans