class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            grouped[sortedString].append(string)
        return list(grouped.values())