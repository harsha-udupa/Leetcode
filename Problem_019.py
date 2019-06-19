"""Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return head

        wanted = None
        wanted_prev = None
        count = 0
        cur = head
        while cur:
            count += 1
            if count == n:
                wanted = head
            elif count == n+1:
                wanted_prev = head
                wanted = wanted.next
            else:
                if wanted:
                    wanted = wanted.next
                if wanted_prev:
                    wanted_prev = wanted_prev.next
            cur = cur.next
        if wanted:
            if wanted.next and wanted_prev:
                wanted_prev.next = wanted.next
                return head
            elif wanted.next:
                return head.next
            elif wanted_prev:
                wanted_prev.next = None
                return head
            else:
                return None
        else:
            return None

