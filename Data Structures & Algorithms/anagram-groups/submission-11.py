class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            new_word = "".join(sorted(word))
            seen[new_word].append(word)
        return list(seen.values())
