class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_total = 1
        zero_index = None
        l = len(nums)
        for i in range(l):
            num = nums[i]
            if num != 0:
                product_total *= num
            else:
                zero_count += 1
                zero_index = i
                if zero_count > 1:
                    return [0] * l
        if zero_count == 1:
            result = [0] * l
            result[zero_index] = product_total
            return result
        result = [product_total//num for num in nums]
        return result
        
                    
        
        
        