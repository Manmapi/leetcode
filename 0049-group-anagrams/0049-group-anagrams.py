class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            str_map[hash("".join(sorted(s)))].append(s)
        return list(str_map.values())