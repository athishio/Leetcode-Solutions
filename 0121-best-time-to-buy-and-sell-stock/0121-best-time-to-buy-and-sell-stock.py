class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice=float('inf')
        maxprofit=0
        for i in prices:
            minprice=min(minprice,i)
            maxprofit=max(maxprofit,i-minprice)
        return maxprofit