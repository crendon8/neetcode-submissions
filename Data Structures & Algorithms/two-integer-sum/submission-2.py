class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remain = target - nums[i]
            idxs = [j for j, val in enumerate(nums) if val == remain and i != j]
            if idxs:
                return [i, idxs[-1]]