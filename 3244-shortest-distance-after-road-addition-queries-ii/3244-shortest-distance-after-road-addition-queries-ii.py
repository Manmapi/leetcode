class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        next_node = list(range(1, n))
        count = n - 1
        result = []
        for x, y in queries:
            while next_node[x] < y:
                tmp = next_node[x]
                next_node[x] = y
                x = tmp
                count -=1
            result.append(count)
        return result