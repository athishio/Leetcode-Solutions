class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def dsum(x):
            s=0
            while x:
                s+=x%10
                x//=10
            return s
        n=len(nums)
        arr=sorted((dsum(x),x) for x in nums)
        d={a[1]:i for i,a in enumerate(arr)}
        ans=n
        vis=[False]*n
        for i in range(n):
            if not vis[i]:
                ans-=1
                j=i
            while not vis[j]:
                vis[j]=True
                j=d[nums[j]]
        return ans