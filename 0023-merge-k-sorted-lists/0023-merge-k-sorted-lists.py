# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2List(node1, node2):
            if not node2:
                return node1
            if not node1:
                return node2
            if node1.val > node2.val:
                node1, node2 = node2, node1
            result = node1
            curr = result
            while node2:
                while curr and curr.next and curr.next.val <= node2.val:
                    curr = curr.next
                if not curr.next:
                    break
                tmp = node2
                node2 = node2.next
                tmp.next = curr.next
                curr.next = tmp
                curr = tmp
            if node2:
                curr.next = node2
            return result
            
        while len(lists) > 1:
            new_lists = []
            n = len(lists)
            for i in range(0, len(lists), 2):  
                if i != n - 1:
                    new_lists.append(merge2List(lists[i], lists[i + 1]))
                else:
                    new_lists.append(merge2List(lists[i], None))
            lists = new_lists
        return lists[0] if lists else None


