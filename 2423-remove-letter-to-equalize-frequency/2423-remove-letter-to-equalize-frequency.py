class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        value = counter.values()
        value_counter = Counter(value)
        x = [[k, v] for k,v in value_counter.items()]
        if len(x) > 2:
            return False
        if len(x) == 1 and x[0][0] != 1 and x[0][1] != 1:
            return False
        if len(x) == 2: 
            if (x[0][0] == 1 and x[0][1] == 1) or (x[1][0] == 1 and x[1][1] == 1):
                return True
            if abs(x[0][0] - x[1][0]) != 1:
                return False
            if x[0][1] != 1 and x[1][1] != 1:
                return False
        return True    