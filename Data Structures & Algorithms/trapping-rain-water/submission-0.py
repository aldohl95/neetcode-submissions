class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0;
        right = len(height) - 1
        res = 0
        Maxl = 0
        Maxr = 0

        while left <= right:
            if Maxl <= Maxr:
                if height[left] > Maxl:
                    Maxl = height[left]
                else:
                    res = res + (Maxl - height[left])
                left += 1
            else:
                if height[right] > Maxr:
                    Maxr = height[right]
                else:
                    res = res + (Maxr - height[right])
                right -= 1

        return res
