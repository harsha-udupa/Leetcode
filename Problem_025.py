"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:


        def reverse_it(head):
            tail = head
            prev = None
            next_cur = head.next
            while next_cur:
                head.next = prev
                prev = head
                head = next_cur
                next_cur = next_cur.next
            head.next = prev
            return head,tail

        if k < 1:
            return head
        cur = head
        t_head = head
        t_tail = None
        p_cur = n_cur = None
        count = 0
        while cur:
            count += 1
            if count == k:
                t_tail = cur
                n_cur = cur.next
                t_tail.next = None
                if p_cur:
                    p_cur.next = None
                t_head, t_tail = reverse_it(t_head)
                if p_cur:
                    p_cur.next = t_head
                else:
                    head = t_head
                t_tail.next = n_cur
                p_cur = t_tail
                t_head = n_cur
                cur = t_tail
                count = 0
            cur = cur.next

        return head
