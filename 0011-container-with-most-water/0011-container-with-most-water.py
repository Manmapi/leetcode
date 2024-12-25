class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        max_left = 0
        for i in range(n):
            v = height[i]
            if v > max_left: 
                max_left = v
            else:
                continue
            for j in range(n - 1, -1, -1):
                val = min(v, height[j]) * (j - i)
                if val > result:
                    result = val
                if height[j] >= v:
                    break    
        return result
