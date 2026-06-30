# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        
        slow = head
        fast = slow.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next

            if fast.next:
                fast = fast.next
            
        return False
