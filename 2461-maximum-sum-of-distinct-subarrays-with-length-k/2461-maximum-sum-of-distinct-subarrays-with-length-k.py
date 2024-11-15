class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        result = 0
        visited = set()
        curr = 0
        while r < len(nums):
            if nums[r] in visited:
                while nums[l] != nums[r]:
                    visited.remove(nums[l])
                    curr -= nums[l]
                    l += 1
                visited.remove(nums[l])
                curr -= nums[l]
                l += 1    
            curr += nums[r]
            visited.add(nums[r])
            if r - l == k - 1:
                result = max(curr, result)
                curr -= nums[l] 
                visited.remove(nums[l])
                l += 1
            r += 1
        return result
