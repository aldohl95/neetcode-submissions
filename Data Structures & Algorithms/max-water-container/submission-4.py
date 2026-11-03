class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = float('-inf')
        l, r = 0, len(heights)-1

        while l < r:
            curr = min(heights[l], heights[r]) * len(heights[l:r])
            result = max(result, curr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result