class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = []
        curr = 0
        track = defaultdict(int)
        for i in range(n):
            track[A[i]] += 1
            if track[A[i]] == 2:
                curr += 1
            track[B[i]] += 1
            if track[B[i]] == 2:
                curr += 1
            result.append(curr)
        return result