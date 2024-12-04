class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        l = 0
        previous = nums[0]
        p = []
        for i in range(1, len(nums)):
            if (nums[i]+previous) % 2 == 0:
                p.append([l,i-1])
                l = i
            previous = nums[i]
        p.append([l,len(nums)-1])
        res = []
        for q in queries:
            l, r = 0, len(p)-1
            i = 0
            while l<=r:
                m = (l+r+1)//2
                if q[0] >= p[m][0]:
                    i = m
                    l = m+1
                else:
                    r = m-1
            if q[1] <= p[i][1]:
                res.append(True)
            else:
                res.append(False)
        return res

