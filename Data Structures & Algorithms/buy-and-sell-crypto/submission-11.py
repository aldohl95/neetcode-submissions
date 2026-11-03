class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        result = 0
        l = 0
        r = 0

        while r < len(prices):
            while r < len(prices) and prices[l] < prices[r]:
                low = min(low, prices[l])
                current = prices[r] - low
                result = max(current, result)
                r+=1
            l = r
            r = l+1
            

        return result

