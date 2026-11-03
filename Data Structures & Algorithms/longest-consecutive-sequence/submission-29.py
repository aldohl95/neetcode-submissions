class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        result = 0

        for num in new_set:
            curr = 1
            if num - 1 not in new_set:
                while num + 1 in new_set:
                    curr += 1
                    num += 1
            result = max(curr, result)

        return result
            
        