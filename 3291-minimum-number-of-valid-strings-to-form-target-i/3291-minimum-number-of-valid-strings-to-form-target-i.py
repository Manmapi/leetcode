class Trie:
    def __init__(self):
        self.child = {}
    
    def insert(self, word):
        curr = self.child
        for w in word:
            if w in curr:
                curr = curr[w]
            else:
                curr[w] = {}
                curr = curr[w]
        curr["end"] = True
    
    def max_length(self, word):
        curr = self.child
        result = 0
        for w in word:
            if w in curr:
                curr = curr[w]
                result += 1
            else:
                return result
        return result
        
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        n = len(target)
        prefix = []
        for i in range(n):
            word = target[i:]
            length = trie.max_length(word)
            if length > 0:
                prefix.append((i, i + length))
        if not prefix:
            return -1
        start, end = prefix[0]
        if start != 0:
            return -1
        next_end = end
        result = 1
        for s, e in prefix[1:]:
            if s < end:
                next_end = max(e, next_end)
            elif s == end:
                result += 1
                end = max(e, next_end)
                next_end = end
            else:
                if next_end >= s:
                    result += 1
                    end = next_end
                    next_end = max(e, end)
                else:
                    return -1
        if next_end < n:
            return -1
        if end < n:
            return result + 1
        return result