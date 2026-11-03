class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        result = []

        result.append(prefix)
        for i in range(len(nums) - 1):
            prefix = prefix * nums[i]
            result.append(prefix)
        
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
        return result