class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        result = 0

        for r in range(len(s)):
            seen[s[r]] += 1

            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            
            result = max(r - l + 1, result)
        return result