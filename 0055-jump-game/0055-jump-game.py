class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reach=0
        last=len(nums)-1
        for i, jump in enumerate(nums):
            if i>reach:
                return False
            reach=max(reach,i+jump)
            if i>=last:
                return True
        return True