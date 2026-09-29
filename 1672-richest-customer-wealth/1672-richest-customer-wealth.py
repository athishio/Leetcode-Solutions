class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x=0
        for i in accounts:
            x=max(x,sum(i))
        return x
