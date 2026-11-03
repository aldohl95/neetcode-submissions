class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        middle = left + 1
        right = middle + 1
        track = {}

        while left < len(nums) - 2:
            while middle < len(nums) - 1:
                while right < len(nums):
                    current = tuple(sorted([nums[left], nums[middle],nums[right]]))
                    if nums[left] + nums[middle] + nums[right] == 0 and current not in track:
                        track[current] = 1
                    right += 1
                middle += 1
                right = middle + 1
            
            left += 1
            middle = left + 1
            right = middle + 1
        return list(track.keys())