class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setList = set(nums)
        result = 0

        for num in setList:
            curr = 1
            n = num
            if (n - 1) not in setList:
                while (n + 1) in setList:
                    curr += 1
                    n += 1
            result = max(curr, result)
        return result
        