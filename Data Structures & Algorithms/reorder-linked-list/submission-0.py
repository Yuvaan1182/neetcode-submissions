# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get second half of list
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        
        # split the list in two halves
        curr = s.next
        s.next = None
        
        # reverse 2nd half of list
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge first and second half
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1

            first, second = tmp1, tmp2

        
        
        
        