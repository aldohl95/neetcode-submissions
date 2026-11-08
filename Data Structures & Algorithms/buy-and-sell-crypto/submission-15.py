class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 0
        res = 0

        while r < len(prices):
            while r < len(prices) and prices[l] < prices[r]:
                total = prices[r] - prices[l]
                res = max(total, res)
                r += 1
            l = r
            r = l + 1
        return res

                
