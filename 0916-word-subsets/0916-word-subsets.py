class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def isSubsets(counter_a, b):
            counter_b = Counter(b)
            for k, v in counter_a.items():
                if counter_b.get(k, 0) < v:
                    return False
            return True
        counter = defaultdict(int)
        for word in words2:
            counter_w = Counter(word)
            for k, v in counter_w.items():
                counter[k] = max(counter[k], v)
        
        return [word for word in words1 if isSubsets(counter, word)]
