class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        visited = set()
        for value in counter.values():
            if value in visited:
                return False
            visited.add(value)
        return True