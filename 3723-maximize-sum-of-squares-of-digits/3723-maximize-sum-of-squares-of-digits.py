class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""
        ans = ""
        while sum > 0:
            digit = min(9, sum)
            ans += str(digit)
            sum -= digit
        ans += "0" * (num - len(ans))
        return ans