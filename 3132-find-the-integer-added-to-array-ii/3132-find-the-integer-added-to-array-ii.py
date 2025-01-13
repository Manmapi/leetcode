class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums2)
        val = nums2[0] - nums1[0]
        def check(diff):
            error = 0
            x = y = 0
            while y < n:
                if nums2[y] - nums1[x] == diff:
                    x += 1
                    y += 1
                else:
                    x += 1 
                    error += 1
                    if error > 2:
                        return False
            return True
        result = float('inf')
        for i in range(3):
            val = nums2[0] - nums1[i]
            if check(val):
                result = min(result, val)
        return result