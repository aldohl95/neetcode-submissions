class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = sorted(s)
        tSorted = sorted(t)

        if sSorted != tSorted:
            return False
        return True
