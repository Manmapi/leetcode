class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Sliding window and update value
        bit_map = {i: 0 for i in range(31)}
        n = len(nums)
        l = r = 0
        curr = 0
        result = n + 1
        while r < n:
            # Update bit_map
            num = nums[r]
            # There are total 30 bit to check
            for i in range(31):
                if (1 << i) & num:
                    bit_map[i] += 1
                    if bit_map[i] == 1:
                        curr += 1 << i
            r += 1
            if curr >= k:
                result = min(result, r - l)
            while curr >= k and l < r - 1:
                minus_nums = nums[l]
                for i in range(31):
                    if (1 << i) & minus_nums:
                        bit_map[i] -= 1
                        if bit_map[i] == 0:
                            curr -= 1 << i
                l +=1
                if curr >= k:
                    result = min(result, r - l)
        if result == n + 1:
            return -1
        return result
                
