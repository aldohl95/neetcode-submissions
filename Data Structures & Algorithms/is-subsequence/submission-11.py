class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pS , pT = 0, 0
        result = ""

        while pT < len(t) and pS < len(s):
            if s[pS] == t[pT]:
                pS += 1
            pT += 1
        
        if pS == len(s):
            return True
        return False
            

        
            
            
