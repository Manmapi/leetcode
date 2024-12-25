class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = defaultdict(int)
        n = len(grid)
        for row in grid:
            value = "#".join([str(x) for x in row])       
            counter[value] += 1
        result = 0
        for i in range(n):
            value = ""
            for row in grid:
                value += f"{str(row[i])}#"
            value = value[:-1]
            result += counter[value]
        return result