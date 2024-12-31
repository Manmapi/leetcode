class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        th = int(n/2)
        nums_mapping = dict()
        for num in nums:
            nums_mapping[num] = nums_mapping.get(num,0) + 1
        return [key for key in nums_mapping if nums_mapping[key] > th][0]