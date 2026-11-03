class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in h:
                return [h[complement], i]
            h[nums[i]] = i
        return []