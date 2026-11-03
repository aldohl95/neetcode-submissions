class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        highest = 0
        

        while r < len(prices):

            while r < len(prices) and prices[r] > prices[l]:
                highest = max(highest, (prices[r] - prices[l]))
                r += 1
            l += 1
            r = l + 1
        return highest
            

                
                
            
            
            
                
        