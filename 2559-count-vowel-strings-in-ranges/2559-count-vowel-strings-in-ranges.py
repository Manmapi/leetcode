class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Prefix sum. Some
        prefix = [0]
        vowels = {
            'a', 'e', 'i', 'o', 'u'
        }
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        return [prefix[y + 1] - prefix[x] for x, y in queries]    