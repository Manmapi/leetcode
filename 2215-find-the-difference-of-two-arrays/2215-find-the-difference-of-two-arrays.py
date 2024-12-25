class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = set(nums1)
        y = set(nums2)
        common = x.intersection(y)
        return [
            list(x - common),
            list(y - common)
        ]
