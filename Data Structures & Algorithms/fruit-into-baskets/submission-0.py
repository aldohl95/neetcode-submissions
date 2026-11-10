class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        basket = defaultdict(int)

        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            res = max(res, sum(basket.values()))
        return res