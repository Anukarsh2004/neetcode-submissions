class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        l = r = head
        before = None

        for _ in range(left - 1):
            before = l
            l = l.next

        for _ in range(right - 1):
            r = r.next

        after = r.next
        prev = after
        curr = l

        while curr != after:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        if before:
            before.next = prev
            return head

        return prev
        