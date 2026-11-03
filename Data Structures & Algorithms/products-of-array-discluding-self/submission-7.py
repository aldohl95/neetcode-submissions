class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        result = []

        result.append(prefix)
        for i in range(len(nums) - 1):
            prefix = nums[i] * prefix
            result.append(prefix)

        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
        
        return result


    
        
            
