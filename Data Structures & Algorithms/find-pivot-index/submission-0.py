class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        for i in range(1, n):
            pref[i] = nums[i-1] + pref[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] + suff[i+1]

        for i in range(0, n):
            if pref[i] == suff[i]:
                return i
        return -1