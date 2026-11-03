class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        swapT, swapS = {}, {}
         
        for i in range(len(s)):
            if s[i] in swapS and swapS[s[i]] != t[i]:
                return False
            if t[i] in swapT and swapT[t[i]] != s[i]:
                return False
            swapS[s[i]] = t[i]
            swapT[t[i]] = s[i]
        return True