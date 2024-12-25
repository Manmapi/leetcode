# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and slow pickleball 
        fast, slow = head, head
        pre_slow = None
        if head.next == None:
            return None
        while fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        pre_slow.next = pre_slow.next.next
        return head 