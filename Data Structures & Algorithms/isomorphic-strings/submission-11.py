class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #foo
        #bar
        sT = {}
        tS = {}

        for i in range(len(s)):
            if s[i] not in sT:
                sT[s[i]] = t[i]
            if t[i] not in tS:
                tS[t[i]] = s[i]
            if sT[s[i]] != t[i] or tS[t[i]] != s[i]:
                return False
        return True 
