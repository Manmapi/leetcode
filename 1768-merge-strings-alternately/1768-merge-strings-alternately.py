class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_1 = len(word1)
        l_2 = len(word2)
        l = min(l_1, l_2)
        result = ""
        for i in range(l * 2):
            if i % 2:
                result += word2[i//2]
            else: 
                result += word1[i//2]
        if l_1 > l_2:
            result += word1[l:]
        if l_2 > l_1:
            result += word2[l:]
        return result
