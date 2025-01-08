class Trie:
    def __init__(self):
        self.child = {}

    def insert(self, index, word: str) -> None:
        curr = self.child
        idxs = set()
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
            if "idxs" in curr:
                idxs |= curr["idxs"]
        if "idxs" not in curr:
            curr["idxs"] = set()
        curr["idxs"].add(index)
        return idxs

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        trie_revert = Trie()
        n = len(words)
        result = 0
        for i, word in enumerate(words):
            idxs = trie.insert(i, word)
            idxs_revert = trie_revert.insert(i, word[::-1])
            val = len(idxs.intersection(idxs_revert))
            result += val
        return result