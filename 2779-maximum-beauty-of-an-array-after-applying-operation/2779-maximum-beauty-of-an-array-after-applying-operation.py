class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        stack = deque([[nums[0], 1]])
        curr = 1
        result = 1
        for num in nums[1:]:
            if num - stack[0][0] <= 2 * k:
                if num > stack[-1][0]:
                    stack.append([num, 1])
                elif num == stack[-1][0]:
                    stack[-1][1] += 1
            else:
                while stack and num - 2 * k > stack[0][0]:
                    value, count = stack.popleft()
                    curr -= count
                stack.append([num, 1])
            curr += 1
            result = max(curr, result)
        return result