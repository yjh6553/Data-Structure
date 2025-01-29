# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        check = head
        length = 1
        while check.next:
            check = check.next
            length += 1
        
        
        num = k % length

        for _ in range(num):
            before_tail = head
            while before_tail.next.next:
                before_tail = before_tail.next
            tail = before_tail.next
            tail.next = head
            head = tail
            before_tail.next = None
        
        return head

        # Time : O(n)
        # Space: O(1)