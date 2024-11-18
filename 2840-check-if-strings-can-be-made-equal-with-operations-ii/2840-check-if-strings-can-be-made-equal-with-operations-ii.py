class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter1 = Counter([s1[i] for i in range(n) if i % 2])
        counter2 = Counter([s2[i] for i in range(n) if i % 2])
        if counter1 != counter2:
            return False
        counter1 = Counter([s1[i] for i in range(n) if i % 2 == 0])
        counter2 = Counter([s2[i] for i in range(n) if i % 2 == 0])
        if counter1 != counter2:
            return False
        return True