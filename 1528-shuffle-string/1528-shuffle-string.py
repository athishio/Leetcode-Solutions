class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t=[""]*len(s)
        for i in range(len(s)):
            t[indices[i]]=s[i]
        return "".join(t)