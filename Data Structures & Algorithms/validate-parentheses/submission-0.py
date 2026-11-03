class Solution:
    def isValid(self, s: str) -> bool:
        clos = {')': '(',']':'[','}': '{'}
        res = []
        

        for string in s:
            if string in clos:
                if res and res[-1] == clos[string]:
                    res.pop()
                else:
                    return False
            else:
                res.append(string)

        if len(res) == 0:
            return True
        else:
            return False

                
