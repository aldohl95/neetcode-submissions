class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wl = int(s[i:j])
            result.append(s[j+1 : j + 1 + wl])
            i = j + 1 + wl
        return result

            

    
