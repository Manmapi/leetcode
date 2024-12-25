# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_end = head
        count = 0
        while odd_end.next and odd_end.next.next:
            odd_end = odd_end.next.next
            count += 1
        even_end = None
        if odd_end.next:
            even_end = odd_end.next 
            odd_end.next = None
        odd = head
        while count > 0:
            tmp = odd.next
            odd.next = odd.next.next
            odd = odd.next
            tmp.next = None
            odd_end.next = tmp
            odd_end = odd_end.next
            count -= 1
        if even_end:
            odd_end.next = even_end 
        return head
            