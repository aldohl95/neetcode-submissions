class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        postfix = 1
        
        result.append(prefix)
        for i in range(len(nums) - 1):
            prefix = prefix * nums[i]
            result.append(prefix)
        for i in range(len(result)-1,-1, -1):
            result[i] = postfix * result[i]
            postfix = postfix * nums[i]

        return result