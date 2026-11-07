class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for string in strs:
            sortedString = " ".join(sorted(string))
            seen[sortedString].append(string)
        return list(seen.values())
