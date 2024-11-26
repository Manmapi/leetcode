class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        x = floor(sqrt(red))
        y = floor(sqrt(blue + 0.25) - 0.5)

        a = floor(sqrt(blue))
        b = floor(sqrt(red + 0.25) - 0.5)

        return max(
            min(x, y) * 2 + int(x > y),
            min(a, b) * 2 + int(a > b)
        )
        