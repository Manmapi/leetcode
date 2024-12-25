class Trie:

    def __init__(self):
        self.child = {}

    def insert(self, word: str) -> None:
        curr = self.child
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["#"] = True

    def search(self, word: str):
        curr = self.child
        for c in word:
            if c not in curr:
                return []
            curr = curr[c]
        result = []
        
        result.extend(self.search_next("", curr)[:3])
        return [word + x for x in result]

    def search_next(self, key, curr):
        next_chars = list(curr.keys())
        next_chars.sort()
        next_chars = next_chars[:3] 
        next_results = []
        if curr.get("#", False):
            next_results.append("")
        for next_char in next_chars:
            if next_char == "#":
                continue
            next_results.extend(self.search_next(next_char, curr[next_char]))
            if len(next_results) >= 3:
                break 
        return [key + x for x in next_results[:3]]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        val = ""
        result = []
        for c in searchWord:
            val += c
            result.append(trie.search(val))
        return result
