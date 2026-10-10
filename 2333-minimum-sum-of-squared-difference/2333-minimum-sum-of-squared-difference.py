class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diff) <= k:
            return 0
        left, right = 0, max(diff)
        while left < right:
            mid = (left + right) // 2
            operations = sum(max(d - mid, 0) for d in diff)
            if operations <= k:
                right = mid
            else:
                left = mid + 1
        for i, d in enumerate(diff):
            k -= max(0, d - left)
            diff[i] = min(d, left)
        for i in range(len(diff)):
            if k == 0:
                break
            if diff[i] == left:
                diff[i] -= 1
                k -= 1
        return sum(d * d for d in diff)