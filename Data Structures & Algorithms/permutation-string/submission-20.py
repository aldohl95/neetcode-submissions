class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        word = "".join(sorted(s1))
        l, r = 0, len(s1)

        while r <= len(s2):
            if word == "".join(sorted(s2[l:r])):
                return True
            l += 1
            r += 1
        return False
        