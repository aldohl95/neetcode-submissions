class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 1
        result = 0
        l, r = 0, 0

        while r < len(s):
            
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
                length += 1
            seen.remove(s[l])
            l += 1
            length -= 1
            result = max(length, result)
        return result
            
                