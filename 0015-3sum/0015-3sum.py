class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        result = []
        for i in range(len_nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len_nums - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    left = nums[l]
                    right = nums[r]
                    result.append([nums[i], nums[l], nums[r]])
                    while l < len_nums and nums[l] == left :
                        l += 1
                    while r >= 0 and nums[r] == right:
                        r -= 1 
            
        return result