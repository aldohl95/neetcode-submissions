class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}

        for i in range(len(s)):
            if s[i] not in st:
                st[s[i]] = t[i]
            if t[i] not in ts:
                ts[t[i]] = s[i]
            
            if s[i] != ts[t[i]] or t[i] != st[s[i]]:
                return False
        return True