class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            t = "".join(sorted(s))
            if t in h:
                h[t].append(s)
            else:
                h[t] = [s]
            
        return list(h.values())
            
            