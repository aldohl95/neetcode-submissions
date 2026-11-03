class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            current = (min(heights[left],heights[right]) * abs(left - right))
            res = max(res, current)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return res
            
        