class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqMagazine = defaultdict(int)
        
        if len(magazine) < len(ransomNote):
            return False
        for char in magazine:
            freqMagazine[char] += 1
        for char in ransomNote:
            if freqMagazine[char] == 0:
                return False
            else:
                freqMagazine[char] -= 1
        return True
