class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["."] * m for _ in range(n)]
        # Loop over each from right to left 
        for i, row in enumerate(box):
            block = n
            for j in range(n - 1, -1, -1):
                r = row[j]
                if r == "#":
                    result[block - 1][m - 1 - i] = "#"
                    block -= 1
                elif r == "*":
                    result[j][m - 1 - i] = "*"
                    block = j
        return result