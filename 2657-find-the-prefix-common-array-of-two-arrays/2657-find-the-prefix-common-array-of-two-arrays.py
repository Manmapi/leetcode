class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = []
        curr = 0
        a = defaultdict(int)
        b = defaultdict(int)
        for i in range(n):
            if A[i] not in a:
                a[A[i]] += 1
                if A[i] in b:
                    curr += 1
            if B[i] not in b:
                b[B[i]] += 1
                if B[i] in a:
                    curr += 1
            result.append(curr)
        return result