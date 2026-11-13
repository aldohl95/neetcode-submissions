class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        fib = defaultdict(int)
        for r in range(len(fruits)):
            fib[fruits[r]] += 1

            while len(fib) > 2:
                fib[fruits[l]] -= 1
                if fib[fruits[l]] == 0:
                    del fib[fruits[l]]
            
                l += 1
            
            res = max(res, sum(fib.values()))
        
        return res