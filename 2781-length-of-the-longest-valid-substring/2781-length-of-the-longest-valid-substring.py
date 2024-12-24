class Trie:
    def __init__(self):
        self.child = {}


    def insert(self, value):
        curr = self.child
        for c in value:
            if c not in curr:
                curr[c] = {} 
            curr = curr[c]
        curr["end"] = True

    def find(self, value):
        index = 0
        curr = self.child
        for c in value:
            if c not in curr:
                return None
            curr = curr[c]
            if curr.get("end", False) == True:
                return index
            index += 1
        return None

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # Trie
        trie = Trie()
        for w in forbidden:
            trie.insert(w)
        n = len(word)
        forbidden_location = []
        result = n*(n + 1) // 2
        for i in range(n):
            val = word[i:i + 10]
            index = trie.find(val)
            if index is not None:
                forbidden_location.append([i, i + index])
        forbidden_location.sort(key=lambda x: x[1])
        m = len(forbidden_location)
        if m == 0:
            return n
        result = 0
        start = 0
        index = 0
        for i in range(n):
            while i >= forbidden_location[index][1]:
                start = max(start, forbidden_location[index][0] + 1)
                index += 1
                if index == m:
                    return max(n - start, result)
            result = max(i - start + 1, result)
        result = max(n - start, result)
        return result