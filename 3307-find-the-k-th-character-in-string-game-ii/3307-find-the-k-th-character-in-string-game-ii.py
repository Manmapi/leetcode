class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # a aa aa-bb aabb-aabb aabbaabb-bbccbbcc
        # a ab abab
        def helper(idx):
            if idx == 0:
                return 0
            n = floor(log2(idx))
            half = 2 ** n
            k = idx % half
            op = operations[n]
            if op:
                return 1 + helper(k)
            else:
                return helper(k)
            
        val = helper(k - 1) % 26 
        return chr(97 + val)
