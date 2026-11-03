class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        k = True
        result = 0
        

        for num in s:
            curr = 1
            n = num
            if (num - 1) not in s:
                while (n + 1) in s:
                    curr += 1
                    n += 1
            result = max(result, curr)


        return result


                    

