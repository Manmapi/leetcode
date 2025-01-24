# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2: 
            return list1
        new_node = ListNode(0)
        current = new_node 
        while list1 and list2: 
            if list1.val <= list2.val:
                current.next = ListNode(val=list1.val)                
                list1 = list1.next
            else:
                current.next = ListNode(val=list2.val)
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return new_node.next