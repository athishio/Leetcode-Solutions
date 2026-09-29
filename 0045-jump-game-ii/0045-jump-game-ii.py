class Solution:
    def jump(self, nums: list[int]) -> int:
        jump=0
        curr_end=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i==curr_end:
                jump+=1
                curr_end=farthest
        return jump