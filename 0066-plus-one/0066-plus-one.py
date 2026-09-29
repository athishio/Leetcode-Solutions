class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        for i in digits:
            sum=sum*10+i
        sum+=1
        return [int(ch) for ch in str(sum)]