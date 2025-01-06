class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        s = ""
        for word in words:
            s += word
            s += "#"
        
        for word in words:
            first_index = s.find(word)
            second_index = s.find(word, first_index + 1)
            if second_index != -1:
                result.append(word)
        return result