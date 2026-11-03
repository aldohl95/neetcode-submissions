class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        

        for word in strs:
            Wsort = "".join(sorted(word))
            group[Wsort].append(word)
        result = [values for values in group.values()]
        return result