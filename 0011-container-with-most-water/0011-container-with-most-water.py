class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        result = min(height[l], height[r]) * (r - l)
        while l < r:
            while l < r and height[l] <= height[r]:
                l += 1
                result = max(result, min(height[l], height[r]) * (r - l))
            while l < r and height[r] <= height[l]:
                r -= 1
                result = max(result, min(height[l], height[r]) * (r - l))        
        return result
