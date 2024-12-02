class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if len(colors) < k:
            return 0
        colors = colors + colors[:k - 1]
        n = len(colors)
        l = 0
        curr = 0
        result = 0
        while curr < n - 1: 
            x = curr + 1
            if colors[x] ^ colors[curr]:
                if x - l > k - 1:
                    l += 1
            else:
                l = x
            curr = x
            if curr - l == k - 1:
                result += 1
        return result

