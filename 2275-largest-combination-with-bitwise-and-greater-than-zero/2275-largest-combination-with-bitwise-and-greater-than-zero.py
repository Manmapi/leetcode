class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_map = dict()
        for candidate in candidates:
            n = ceil(log2(candidate))
            for i in range(n + 1):
                if 1 << i & candidate:
                    bit_map[i] = bit_map.get(i, 0 ) + 1
        return max(bit_map.values())