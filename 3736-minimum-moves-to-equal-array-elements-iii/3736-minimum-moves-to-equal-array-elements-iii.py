class Solution:
    def minMoves(self, nums: List[int]) -> int:
        hmax=max(nums)
        count=0
        for i in range(len(nums)):
            while nums[i]<hmax:
                nums[i]=nums[i]+1
                count+=1
        return count