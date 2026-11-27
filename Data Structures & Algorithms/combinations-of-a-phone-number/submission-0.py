class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        lc = ""
        mapped = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtrack(idx):
            nonlocal lc
            if idx == len(digits):
                res.append(lc)
                return
            string = mapped[digits[idx]]
            for i in range(len(string)):
                lc += string[i]
                backtrack(idx + 1)
                lc = lc[:-1]
            
        backtrack(0) 
        return res

