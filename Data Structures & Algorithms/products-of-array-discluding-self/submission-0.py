class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        numbers = {}
        product = 1

        for i in range(len(nums)):
            numbers[i] = nums[i]
        

        for i in range(len(nums)):
            for key, value in numbers.items():
                if key != i:
                    product = product * value
                    
            res.append(product)
            product = 1
        
        return res
                
            

