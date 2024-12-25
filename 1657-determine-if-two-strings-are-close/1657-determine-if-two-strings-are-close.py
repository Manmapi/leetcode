class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1).values()
        freq2 = Counter(word2).values()
        
        return set(word1) == set(word2) and Counter(freq1) == Counter(freq2)