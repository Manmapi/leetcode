class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        result = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l_curr = height[l]
                while l < r and height[l] <= l_curr:
                    l += 1
                result = max(result, min(height[l], height[r]) * (r - l))
            else:
                r_curr = height[r]
                while l < r and height[r] <= r_curr:
                    r -= 1
                result = max(result, min(height[l], height[r]) * (r - l))        
        return result
