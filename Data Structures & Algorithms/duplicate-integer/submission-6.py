class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = set(nums)
        if len(newList) != len(nums):
            return True
        else:
            return False