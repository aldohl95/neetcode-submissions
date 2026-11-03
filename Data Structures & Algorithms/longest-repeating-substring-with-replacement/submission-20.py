class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)

            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] = seen.get(s[l]) - 1
                l+=1
            result = max(result, (r - l + 1))

        return result