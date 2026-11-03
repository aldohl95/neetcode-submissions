class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        result = 0

        while l < len(prices) - 1:
            while r < len(prices) and prices[l] < prices[r]:
                current = prices[r] - prices[l]
                result = max(result, current)
                r += 1
            l = r
            r = l + 1
        return result


        