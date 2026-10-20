class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            s=sum(int(n) for n in str(num))
            if s==i:
                return i
        return -1