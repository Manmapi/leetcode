# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        n = len(values)
        max_ = 0
        for i in range(n // 2):
            max_ = max(max_, values[i] + values[n - i -1])
        return max_