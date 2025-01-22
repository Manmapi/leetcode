class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        result = [x for x in nums]
        q = []
        def find(target):
            l, r = 0, len(q) - 1
            found = False
            while l <= r:
                mid = (l + r) // 2
                if q[mid][0] > target:
                    if q[mid][0] - target <= limit: 
                        found = True
                    r = mid - 1
                    
                else:
                    l = mid + 1
            if found:
                return l
            else:
                return None
        for i, num in enumerate(nums):
            while (found := find(num)) is not None:
                value, index = q[found]
                result[index], result[i] = num, value
                q[found][0] = num
                num = value
            bisect.insort_left(q, [num, i])
            print(q, num, i, found)

        return result