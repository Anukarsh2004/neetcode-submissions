# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        l = r = head

        before = None

        for _ in range(left-1):
            before = l
            l = l.next
        
        for _ in range(right-1):
            r = r.next
        
        print(l.val)
        print(r.val)
        

        stop = r.next
        prev = r.next
        curr = l

        while curr != stop:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        if before:
            before.next = prev
            return head

        return prev

        